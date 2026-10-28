# -*- coding: utf-8 -*-
"""
KrishiMitra AI — Intelligent Farming Assistant
Full-Stack Flask Application
"""

import os
import uuid
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Flask, render_template, request, redirect, url_for, flash,
    jsonify, session, g
)
from flask_login import (
    LoginManager, login_user, login_required, logout_user, current_user
)

from config import Config
from models import db, User, DiseasePrediction, FarmingQuery, MarketBookmark
from models import FarmBoundary, SatelliteAnalysis
from translations import get_text, TRANSLATIONS
from disease_knowledge_base import CLASS_NAME_LIST, get_disease_info
from inference_engine import predict_disease
from weather_service import WeatherService
from schemes_data import get_all_schemes, get_scheme_by_id, evaluate_eligibility
from market_service import MarketService
from forecast_service import PriceForecastService
from assistant_service import FarmingAssistant


# ── Module 9 imports (satellite feature) ─────────────────────────────────────
from satellite_service import (
    SatelliteService, compute_area_hectares, credentials_configured, NDVI_THRESHOLDS
)
from satellite_zones import compute_zone_grid, summarise_anomalies

# ================= APPLICATION FACTORY =================

app = Flask(__name__)
app.config.from_object(Config)

# Ensure upload directory exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Database
db.init_app(app)

# Ensure all database tables exist (safe: create_all only creates missing tables,
# never drops or modifies existing ones with existing data)
with app.app_context():
    db.create_all()

# Login Manager
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Please sign in to access this feature."
login_manager.login_message_category = "info"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# ================= LANGUAGE HELPERS & CONTEXT =================

def get_current_language():
    """Detect current user language: Query param -> Session -> User Profile -> Default 'mr'."""
    # 1. Query parameter
    lang_param = request.args.get("lang")
    if lang_param in ["mr", "en", "hi"]:
        session["lang"] = lang_param
        if current_user.is_authenticated:
            current_user.preferred_language = lang_param
            try:
                db.session.commit()
            except Exception:
                db.session.rollback()
        return lang_param

    # 2. Session
    if "lang" in session and session["lang"] in ["mr", "en", "hi"]:
        return session["lang"]

    # 3. User profile
    if current_user.is_authenticated and current_user.preferred_language:
        session["lang"] = current_user.preferred_language
        return current_user.preferred_language

    # 4. Default: Marathi
    session["lang"] = "mr"
    return "mr"


@app.context_processor
def inject_translations():
    lang = get_current_language()
    def t(key):
        return get_text(key, lang=lang)
    
    return {
        "t": t,
        "current_lang": lang,
        "supported_languages": [
            ("mr", "मराठी"),
            ("en", "English"),
            ("hi", "हिंदी")
        ]
    }


# ================= GENERAL & AUTH ROUTES =================

@app.route("/")
def home():
    """Landing Page with branding, feature overview, and language selection."""
    return render_template("index.html")


@app.route("/set_language/<lang_code>")
def set_language(lang_code):
    """Persists language switch and redirects back to caller."""
    if lang_code in ["mr", "en", "hi"]:
        session["lang"] = lang_code
        if current_user.is_authenticated:
            current_user.preferred_language = lang_code
            db.session.commit()
            
    next_url = request.referrer or url_for("home")
    return redirect(next_url)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Farmer account registration with server-side validation and password hashing."""
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    lang = get_current_language()
    if request.method == "POST":
        fullname = request.form.get("fullname", "").strip()
        email = request.form.get("email", "").strip().lower()
        mobile = request.form.get("mobile", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")
        preferred_language = request.form.get("preferred_language", lang)
        district = request.form.get("district", "Pune").strip()

        # Validation
        if not fullname or not email or not password or not mobile:
            flash(get_text("invalid_credentials", lang), "danger")
            return render_template("register.html")

        if password != confirm_password:
            flash(get_text("passwords_mismatch", lang), "danger")
            return render_template("register.html")

        if len(password) < 6:
            flash("Password must be at least 6 characters long.", "warning")
            return render_template("register.html")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash(get_text("email_exists", lang), "warning")
            return redirect(url_for("login"))

        hashed_pw = generate_password_hash(password)
        new_user = User(
            fullname=fullname,
            email=email,
            mobile=mobile,
            password=hashed_pw,
            preferred_language=preferred_language,
            district=district or "Pune"
        )
        db.session.add(new_user)
        db.session.commit()

        session["lang"] = preferred_language
        flash(get_text("reg_success", preferred_language), "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Farmer login route with session creation."""
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    lang = get_current_language()
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            session["lang"] = user.preferred_language or lang
            return redirect(url_for("dashboard"))

        flash(get_text("invalid_credentials", lang), "danger")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """Sign out user."""
    logout_user()
    return redirect(url_for("login"))


# ================= DASHBOARD ROUTE =================

@app.route("/dashboard")
@login_required
def dashboard():
    """Main farmer dashboard aggregating stats, weather, disease shortcut, and schemes."""
    lang = get_current_language()
    
    # User-specific statistics
    user_predictions = DiseasePrediction.query.filter_by(user_id=current_user.id).order_by(DiseasePrediction.created_at.desc()).all()
    scan_count = len(user_predictions)
    recent_predictions = user_predictions[:5]
    
    # Weather summary for farmer's district
    district = current_user.district or "Pune"
    weather_data = WeatherService.get_weather_data(district)

    # Highlighted schemes
    all_schemes = get_all_schemes()
    featured_schemes = all_schemes[:4]

    return render_template(
        "dashboard.html",
        user=current_user,
        scan_count=scan_count,
        weather=weather_data,
        recent_predictions=recent_predictions,
        featured_schemes=featured_schemes,
        district=district
    )


# ================= MODULE ONE & TWO: DISEASE DETECTION & DUAL TREATMENTS =================

@app.route("/detect")
@login_required
def detect():
    """Plant disease detection and dual treatment recommendations page."""
    return render_template("detect.html", user=current_user)


@app.route("/predict", methods=["POST"])
@login_required
def predict():
    """
    Image upload & live camera inference endpoint.
    Preprocesses leaf image, runs Keras model, attaches dual treatment plans,
    and logs prediction to user history in the database.
    """
    lang = get_current_language()

    if "file" not in request.files:
        return jsonify({"success": False, "error": "No file uploaded. Please upload a leaf image."}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"success": False, "error": "No file selected."}), 400

    # Validate file extension
    ext = file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if ext not in Config.ALLOWED_EXTENSIONS:
        return jsonify({
            "success": False,
            "error": f"Invalid file format '{ext}'. Allowed formats: {', '.join(Config.ALLOWED_EXTENSIONS)}"
        }), 400

    # Secure unique filename
    unique_filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
    save_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
    file.save(save_path)

    # Check file size (<16 MB)
    file_size = os.path.getsize(save_path)
    if file_size > Config.MAX_CONTENT_LENGTH:
        os.remove(save_path)
        return jsonify({"success": False, "error": "File size exceeds 16 MB limit."}), 400

    # Run Real Keras Inference
    model_path = Config.MODEL_PATH
    result = predict_disease(save_path, lang=lang, model_path=model_path)

    if not result.get("success"):
        return jsonify(result), 500

    # Save to user's history in the database
    disease_info = result["disease_info"]
    prediction_record = DiseasePrediction(
        user_id=current_user.id,
        image_filename=unique_filename,
        disease_class=result["class_name"],
        plant_name=disease_info["plant_name"],
        is_healthy=disease_info["is_healthy"],
        confidence=result["confidence"]
    )
    db.session.add(prediction_record)
    db.session.commit()

    # Return prediction with image URL and dual treatment plans
    return jsonify({
        "success": True,
        "prediction_id": prediction_record.id,
        "image_url": url_for("static", filename=f"uploads/{unique_filename}"),
        "class_name": result["class_name"],
        "confidence": result["confidence"],
        "low_confidence": result["low_confidence"],
        "disease_info": disease_info
    })


@app.route("/treatment/<int:prediction_id>")
@login_required
def treatment_detail(prediction_id):
    """View full dual treatment plans for a recorded prediction."""
    lang = get_current_language()
    pred = DiseasePrediction.query.filter_by(id=prediction_id, user_id=current_user.id).first_or_404()
    disease_info = get_disease_info(pred.disease_class, lang=lang)
    
    return render_template(
        "treatment.html",
        prediction=pred,
        disease_info=disease_info,
        user=current_user
    )


# ================= MODULE THREE: WEATHER FORECASTING =================

@app.route("/weather")
@login_required
def weather():
    """Weather forecast and farm advisories view."""
    district = current_user.district or "Pune"
    weather_data = WeatherService.get_weather_data(district)
    return render_template("weather.html", user=current_user, weather=weather_data, city=district)


@app.route("/get_weather", methods=["POST"])
@login_required
def get_weather():
    """Dynamic AJAX weather query by district or village."""
    data = request.get_json() or {}
    city = data.get("city", "").strip() or current_user.district or "Pune"
    weather_data = WeatherService.get_weather_data(city)
    return jsonify(weather_data)


# ================= MODULE FOUR: GOVERNMENT SCHEMES =================

@app.route("/government")
@login_required
def government():
    """Government agricultural schemes portal with categories and search."""
    schemes = get_all_schemes()
    return render_template("government.html", user=current_user, schemes=schemes)


@app.route("/scheme/<scheme_id>")
@login_required
def scheme_detail(scheme_id):
    """Dedicated scheme details view with verified application links."""
    scheme = get_scheme_by_id(scheme_id)
    if not scheme:
        flash("Government scheme not found.", "warning")
        return redirect(url_for("government"))
        
    return render_template("scheme.html", user=current_user, scheme=scheme)


@app.route("/check_eligibility", methods=["POST"])
@login_required
def check_eligibility():
    """Guided eligibility questionnaire endpoint."""
    data = request.get_json() or {}
    land_acres = float(data.get("land_acres", 2.0))
    category = data.get("category", "general")
    irrigation = data.get("irrigation", "drip")
    
    matches = evaluate_eligibility(land_acres, category, irrigation)
    return jsonify({"success": True, "matches": matches})


# ================= MODULE FIVE & SIX: MARKET PRICES & FORECASTING =================

@app.route("/market")
@login_required
def market():
    """Current Mandi Market Prices and 2-3 Months AI/ML Price Forecasting view."""
    supported = MarketService.get_supported_locations()
    initial_price = MarketService.get_market_price(
        state="Maharashtra", district=current_user.district or "Pune", commodity="Tomato"
    )
    initial_forecast = PriceForecastService.generate_price_forecast("Tomato", horizon_months=2)

    return render_template(
        "market.html",
        user=current_user,
        supported=supported,
        initial_price=initial_price,
        initial_forecast=initial_forecast
    )


@app.route("/get_market_price", methods=["POST"])
@login_required
def get_market_price():
    """AJAX endpoint for authentic Mandi prices."""
    data = request.get_json() or {}
    state = data.get("state", "Maharashtra")
    district = data.get("district", "Pune")
    commodity = data.get("commodity", "Tomato")

    result = MarketService.get_market_price(state=state, district=district, commodity=commodity)
    return jsonify(result)


@app.route("/get_price_forecast", methods=["POST"])
@login_required
def get_price_forecast():
    """AJAX endpoint for 2-3 months time-series price trend forecasting."""
    data = request.get_json() or {}
    commodity = data.get("commodity", "Tomato")
    horizon = int(data.get("horizon", 2))

    forecast_data = PriceForecastService.generate_price_forecast(commodity=commodity, horizon_months=horizon)
    return jsonify({"success": True, "forecast": forecast_data})


# ================= MODULE SEVEN: PERSONALIZED FARMING ASSISTANT =================

@app.route("/assistant")
@login_required
def assistant():
    """Personalized Farming Assistant Chat view."""
    # Load recent conversation history for user
    recent_queries = FarmingQuery.query.filter_by(user_id=current_user.id).order_by(FarmingQuery.created_at.desc()).limit(10).all()
    return render_template("assistant.html", user=current_user, recent_queries=recent_queries)


@app.route("/ask_assistant", methods=["POST"])
@login_required
def ask_assistant():
    """AJAX query endpoint for multilingual farming assistant."""
    lang = get_current_language()
    data = request.get_json() or {}
    query_text = data.get("question", "").strip()

    if not query_text:
        return jsonify({"success": False, "error": "Question cannot be empty."}), 400

    profile = {
        "district": current_user.district,
        "crops": current_user.primary_crops,
        "farm_size": current_user.farm_size
    }

    result = FarmingAssistant.get_answer(query_text, lang=lang, user_profile=profile)
    
    # Store query in user's history
    query_rec = FarmingQuery(
        user_id=current_user.id,
        question=query_text,
        answer=result["answer"],
        language=lang
    )
    db.session.add(query_rec)
    db.session.commit()

    return jsonify({
        "success": True,
        "question": query_text,
        "answer": result["answer"],
        "source": result["source"]
    })


# ================= MODULE EIGHT: PROFILE & FARMING HISTORY =================

@app.route("/history")
@login_required
def history():
    """Farmer's complete private diagnostic history."""
    predictions = DiseasePrediction.query.filter_by(user_id=current_user.id).order_by(DiseasePrediction.created_at.desc()).all()
    return render_template("history.html", user=current_user, predictions=predictions)


@app.route("/settings", methods=["GET", "POST"])
@app.route("/profile", methods=["GET", "POST"])
@login_required
def settings():
    """Farmer Profile and Agricultural Settings view."""
    lang = get_current_language()
    if request.method == "POST":
        current_user.fullname = request.form.get("fullname", current_user.fullname).strip()
        current_user.mobile = request.form.get("mobile", current_user.mobile).strip()
        current_user.district = request.form.get("district", current_user.district).strip()
        current_user.state = request.form.get("state", current_user.state).strip()
        
        try:
            current_user.farm_size = float(request.form.get("farm_size", current_user.farm_size))
        except (ValueError, TypeError):
            pass

        current_user.primary_crops = request.form.get("primary_crops", current_user.primary_crops).strip()
        
        pref_lang = request.form.get("preferred_language", current_user.preferred_language)
        if pref_lang in ["mr", "en", "hi"]:
            current_user.preferred_language = pref_lang
            session["lang"] = pref_lang

        db.session.commit()
        flash(get_text("profile_saved", session.get("lang", "mr")), "success")
        return redirect(url_for("settings"))

    return render_template("settings.html", user=current_user)


# ================= DATABASE INITIALIZATION =================

with app.app_context():
    db.create_all()


# ================= MODULE NINE: SATELLITE CROP INTELLIGENCE =================

@app.route("/satellite")
@login_required
def satellite():
    """Satellite Crop Intelligence monitoring page."""
    farms = FarmBoundary.query.filter_by(user_id=current_user.id).order_by(FarmBoundary.created_at.desc()).all()
    latest_analysis = None
    selected_farm = None

    if farms:
        selected_farm = farms[0]
        latest_analysis = (
            SatelliteAnalysis.query
            .filter_by(farm_id=selected_farm.id, user_id=current_user.id)
            .order_by(SatelliteAnalysis.analyzed_at.desc())
            .first()
        )

    return render_template(
        "satellite.html",
        user=current_user,
        farms=[f.to_dict() for f in farms],
        selected_farm=selected_farm.to_dict() if selected_farm else None,
        latest_analysis=latest_analysis.to_dict() if latest_analysis else None,
        cdse_configured=credentials_configured(),
        ndvi_thresholds=NDVI_THRESHOLDS,
    )


@app.route("/satellite/farms", methods=["GET"])
@login_required
def satellite_list_farms():
    """Returns the authenticated user's saved farm boundaries as JSON."""
    farms = FarmBoundary.query.filter_by(user_id=current_user.id).order_by(FarmBoundary.created_at.desc()).all()
    return jsonify({"success": True, "farms": [f.to_dict() for f in farms]})


@app.route("/satellite/farms", methods=["POST"])
@login_required
def satellite_save_farm():
    """
    Saves a new farm boundary.
    Expects JSON: { farm_name, crop_type, crop_variety, sowing_date, boundary_geojson, notes }
    boundary_geojson must be a GeoJSON Polygon string.
    """
    import json as _json

    data = request.get_json() or {}
    farm_name = data.get("farm_name", "My Farm").strip()[:120]
    crop_type = data.get("crop_type", "Tomato").strip()[:80]
    crop_variety = (data.get("crop_variety") or "").strip()[:120] or None
    sowing_date = (data.get("sowing_date") or "").strip()[:20] or None
    boundary_raw = data.get("boundary_geojson", "")
    notes = (data.get("notes") or "").strip()[:500] or None

    # Validate boundary
    if not boundary_raw:
        return jsonify({"success": False, "error": "Farm boundary geometry is required."}), 400

    try:
        polygon = _json.loads(boundary_raw) if isinstance(boundary_raw, str) else boundary_raw
        coords = polygon.get("coordinates", [[]])[0]
        if len(coords) < 4:
            raise ValueError("Polygon must have at least 3 vertices + closing point.")
        for pt in coords:
            if not (-180 <= pt[0] <= 180) or not (-90 <= pt[1] <= 90):
                raise ValueError(f"Invalid coordinate: {pt}")
    except (ValueError, KeyError, TypeError) as exc:
        return jsonify({"success": False, "error": f"Invalid boundary geometry: {exc}"}), 400

    # Compute centroid and area
    lons = [c[0] for c in coords]
    lats = [c[1] for c in coords]
    center_lat = sum(lats) / len(lats)
    center_lon = sum(lons) / len(lons)
    area_ha = compute_area_hectares(polygon)

    boundary_json_str = _json.dumps(polygon)

    farm = FarmBoundary(
        user_id=current_user.id,
        farm_name=farm_name,
        crop_type=crop_type,
        crop_variety=crop_variety,
        sowing_date=sowing_date,
        boundary_geojson=boundary_json_str,
        center_lat=center_lat,
        center_lon=center_lon,
        area_hectares=area_ha,
        notes=notes,
    )
    db.session.add(farm)
    db.session.commit()

    return jsonify({"success": True, "farm": farm.to_dict()})


@app.route("/satellite/farms/<int:farm_id>", methods=["DELETE"])
@login_required
def satellite_delete_farm(farm_id):
    """Deletes a farm boundary owned by the authenticated user."""
    farm = FarmBoundary.query.filter_by(id=farm_id, user_id=current_user.id).first_or_404()
    db.session.delete(farm)
    db.session.commit()
    return jsonify({"success": True})


@app.route("/satellite/analyze/<int:farm_id>", methods=["POST"])
@login_required
def satellite_analyze(farm_id):
    """
    Triggers a full satellite NDVI analysis for the specified farm.
    Retrieves Sentinel-2 data (or demo grid), computes NDVI,
    generates zone analysis, and persists results.
    """
    import json as _json
    import numpy as np

    farm = FarmBoundary.query.filter_by(id=farm_id, user_id=current_user.id).first_or_404()

    # Parse polygon
    try:
        polygon = _json.loads(farm.boundary_geojson)
    except Exception:
        return jsonify({"success": False, "error": "Corrupt farm boundary geometry."}), 400

    # Run satellite analysis
    result = SatelliteService.analyze_farm(farm)

    if result.get("status") == "error":
        return jsonify({"success": False, "error": result.get("error", "Analysis failed.")}), 500

    # ── Rebuild numpy grid for zone analysis ──────────────────────────────────
    from satellite_service import _bbox_from_geojson, _synthetic_ndvi_grid, _point_in_polygon

    bbox = _bbox_from_geojson(polygon)
    resolution = 50

    # Reconstruct ndvi_grid from heatmap_cells for zone analysis
    heatmap_cells = result.get("heatmap_cells", [])
    if heatmap_cells:
        # Rebuild grid from cell list
        lats_set = sorted(set(c["lat"] for c in heatmap_cells))
        lons_set = sorted(set(c["lon"] for c in heatmap_cells))
        lat_arr = np.array(lats_set)
        lon_arr = np.array(lons_set)
        rows = len(lat_arr)
        cols = len(lon_arr)
        lat_idx = {v: i for i, v in enumerate(lats_set)}
        lon_idx = {v: i for i, v in enumerate(lons_set)}

        ndvi_grid = np.full((rows, cols), np.nan)
        field_mask = np.zeros((rows, cols), dtype=bool)
        for cell in heatmap_cells:
            r = lat_idx.get(cell["lat"])
            c = lon_idx.get(cell["lon"])
            if r is not None and c is not None:
                field_mask[r, c] = True
                if cell["ndvi"] is not None:
                    ndvi_grid[r, c] = cell["ndvi"]
    else:
        ndvi_grid, field_mask, lon_arr, lat_arr = _synthetic_ndvi_grid(polygon, bbox, resolution)

    # ── Zone analysis ─────────────────────────────────────────────────────────
    # Load previous analysis for change detection
    prev_analysis = (
        SatelliteAnalysis.query
        .filter_by(farm_id=farm_id, user_id=current_user.id, status="complete")
        .order_by(SatelliteAnalysis.analyzed_at.desc())
        .first()
    )
    prev_zones = _json.loads(prev_analysis.zones_json) if (prev_analysis and prev_analysis.zones_json) else None

    zones = compute_zone_grid(
        ndvi_grid=ndvi_grid,
        field_mask=field_mask,
        lon_steps=lon_arr,
        lat_steps=lat_arr,
        polygon=polygon,
        field_mean=result.get("ndvi_mean"),
        field_std=result.get("ndvi_std"),
        previous_zones=prev_zones,
    )
    anomaly_summary = summarise_anomalies(zones)

    # ── Generate insight text ─────────────────────────────────────────────────
    insight = SatelliteService.generate_insights(result, farm.farm_name, farm.crop_type)

    # ── Persist analysis record ───────────────────────────────────────────────
    status = "demo" if result.get("demo_mode") else "complete"
    analysis_rec = SatelliteAnalysis(
        farm_id=farm.id,
        user_id=current_user.id,
        observation_date=result.get("observation_date"),
        satellite_source=result.get("satellite_source"),
        cloud_cover_pct=result.get("cloud_cover_pct"),
        valid_pixel_pct=result.get("valid_pixel_pct"),
        ndvi_mean=result.get("ndvi_mean"),
        ndvi_min=result.get("ndvi_min"),
        ndvi_max=result.get("ndvi_max"),
        ndvi_std=result.get("ndvi_std"),
        ndvi_distribution_json=_json.dumps(result.get("distribution", {})),
        zones_json=_json.dumps(zones),
        status=status,
        insight_text=insight,
        heatmap_data_json=_json.dumps(heatmap_cells[:2000]),  # cap to avoid DB bloat
    )
    db.session.add(analysis_rec)
    db.session.commit()

    return jsonify({
        "success": True,
        "analysis_id": analysis_rec.id,
        "status": status,
        "demo_mode": result.get("demo_mode"),
        "observation_date": result.get("observation_date"),
        "satellite_source": result.get("satellite_source"),
        "cloud_cover_pct": result.get("cloud_cover_pct"),
        "valid_pixel_pct": result.get("valid_pixel_pct"),
        "ndvi_mean": result.get("ndvi_mean"),
        "ndvi_min": result.get("ndvi_min"),
        "ndvi_max": result.get("ndvi_max"),
        "ndvi_std": result.get("ndvi_std"),
        "distribution": result.get("distribution"),
        "heatmap_cells": heatmap_cells,
        "thresholds": result.get("thresholds"),
        "zones": zones,
        "anomaly_summary": anomaly_summary,
        "insight_text": insight,
    })


@app.route("/satellite/history/<int:farm_id>", methods=["GET"])
@login_required
def satellite_history(farm_id):
    """Returns the last N analysis records for a farm, for historical comparison."""
    farm = FarmBoundary.query.filter_by(id=farm_id, user_id=current_user.id).first_or_404()
    limit = min(int(request.args.get("limit", 10)), 30)
    analyses = (
        SatelliteAnalysis.query
        .filter_by(farm_id=farm_id, user_id=current_user.id)
        .order_by(SatelliteAnalysis.analyzed_at.desc())
        .limit(limit)
        .all()
    )
    history = []
    for a in analyses:
        rec = a.to_dict()
        rec.pop("zones", None)      # too large for history list
        rec.pop("heatmap_data", None)
        history.append(rec)

    return jsonify({"success": True, "farm": farm.to_dict(), "history": history})


# ================= DATABASE INITIALIZATION =================

with app.app_context():
    db.create_all()

# ================= RUN SERVER =================

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
