from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    # Profile information
    preferred_language = db.Column(db.String(10), default="mr")  # 'mr', 'en', 'hi'
    state = db.Column(db.String(80), default="Maharashtra")
    district = db.Column(db.String(80), default="Pune")
    farm_size = db.Column(db.Float, default=2.5)  # in acres
    primary_crops = db.Column(db.String(200), default="Tomato, Onion, Soybean")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    predictions = db.relationship("DiseasePrediction", backref="farmer", lazy=True, cascade="all, delete-orphan")
    queries = db.relationship("FarmingQuery", backref="farmer", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.email}>"


class DiseasePrediction(db.Model):
    __tablename__ = "disease_predictions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    image_filename = db.Column(db.String(255), nullable=False)
    disease_class = db.Column(db.String(100), nullable=False)
    plant_name = db.Column(db.String(80), default="Tomato")
    is_healthy = db.Column(db.Boolean, default=False)
    confidence = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    treatment_viewed = db.Column(db.String(50), default="both")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "disease_class": self.disease_class,
            "plant_name": self.plant_name,
            "is_healthy": self.is_healthy,
            "confidence": self.confidence,
            "image_filename": self.image_filename,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M"),
        }


class FarmingQuery(db.Model):
    __tablename__ = "farming_queries"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(10), default="mr")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class MarketBookmark(db.Model):
    __tablename__ = "market_bookmarks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    commodity = db.Column(db.String(80), nullable=False)
    market = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(80), default="Maharashtra")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ─── Module 9: Satellite Crop Intelligence ────────────────────────────────────

class FarmBoundary(db.Model):
    """
    Stores a farmer's field polygon for satellite crop monitoring.
    One farmer may have multiple saved fields.
    GeoJSON polygon stored as TEXT for portability (no PostGIS dependency needed).
    """
    __tablename__ = "farm_boundaries"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    farm_name = db.Column(db.String(120), nullable=False, default="My Farm")
    crop_type = db.Column(db.String(80), default="Tomato")
    crop_variety = db.Column(db.String(120), nullable=True)
    sowing_date = db.Column(db.String(20), nullable=True)          # ISO date string
    # GeoJSON polygon string: {"type":"Polygon","coordinates":[[[lon,lat],...]]}
    boundary_geojson = db.Column(db.Text, nullable=False)
    # Centroid for quick map rendering
    center_lat = db.Column(db.Float, nullable=False, default=18.52)
    center_lon = db.Column(db.Float, nullable=False, default=73.85)
    area_hectares = db.Column(db.Float, nullable=True)             # Computed on save
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Satellite analysis records linked to this farm
    analyses = db.relationship(
        "SatelliteAnalysis", backref="farm", lazy=True,
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "farm_name": self.farm_name,
            "crop_type": self.crop_type,
            "crop_variety": self.crop_variety,
            "sowing_date": self.sowing_date,
            "boundary_geojson": self.boundary_geojson,
            "center_lat": self.center_lat,
            "center_lon": self.center_lon,
            "area_hectares": round(self.area_hectares, 3) if self.area_hectares else None,
            "notes": self.notes,
            "created_at": self.created_at.strftime("%Y-%m-%d"),
        }


class SatelliteAnalysis(db.Model):
    """
    One row per NDVI analysis run on a FarmBoundary.
    Stores computed NDVI statistics and zone data as JSON strings.
    """
    __tablename__ = "satellite_analyses"

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm_boundaries.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Satellite observation metadata
    observation_date = db.Column(db.String(20), nullable=True)     # ISO date of the Sentinel tile
    satellite_source = db.Column(db.String(50), default="Sentinel-2 L2A")
    cloud_cover_pct = db.Column(db.Float, nullable=True)
    valid_pixel_pct = db.Column(db.Float, nullable=True)           # % pixels not masked

    # NDVI aggregate statistics (from real computation)
    ndvi_mean = db.Column(db.Float, nullable=True)
    ndvi_min = db.Column(db.Float, nullable=True)
    ndvi_max = db.Column(db.Float, nullable=True)
    ndvi_std = db.Column(db.Float, nullable=True)

    # NDVI category distribution (JSON: {"high": 45.2, "good": 30.1, ...})
    ndvi_distribution_json = db.Column(db.Text, nullable=True)

    # Per-zone analysis results (JSON list of zone dicts)
    zones_json = db.Column(db.Text, nullable=True)

    # Analysis status: "pending" | "complete" | "no_data" | "error"
    status = db.Column(db.String(20), default="pending")
    error_message = db.Column(db.Text, nullable=True)

    # AI-generated plain-language insight text
    insight_text = db.Column(db.Text, nullable=True)

    # Heatmap pixel grid (base64 PNG or compact JSON — stored if small enough)
    heatmap_data_json = db.Column(db.Text, nullable=True)

    analyzed_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        import json
        return {
            "id": self.id,
            "farm_id": self.farm_id,
            "observation_date": self.observation_date,
            "satellite_source": self.satellite_source,
            "cloud_cover_pct": self.cloud_cover_pct,
            "valid_pixel_pct": self.valid_pixel_pct,
            "ndvi_mean": round(self.ndvi_mean, 4) if self.ndvi_mean is not None else None,
            "ndvi_min": round(self.ndvi_min, 4) if self.ndvi_min is not None else None,
            "ndvi_max": round(self.ndvi_max, 4) if self.ndvi_max is not None else None,
            "ndvi_std": round(self.ndvi_std, 4) if self.ndvi_std is not None else None,
            "ndvi_distribution": json.loads(self.ndvi_distribution_json) if self.ndvi_distribution_json else {},
            "zones": json.loads(self.zones_json) if self.zones_json else [],
            "status": self.status,
            "error_message": self.error_message,
            "insight_text": self.insight_text,
            "heatmap_data": json.loads(self.heatmap_data_json) if self.heatmap_data_json else None,
            "analyzed_at": self.analyzed_at.strftime("%Y-%m-%d %H:%M"),
        }
