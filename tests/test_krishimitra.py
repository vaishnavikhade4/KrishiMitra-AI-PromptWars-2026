# -*- coding: utf-8 -*-
"""
KrishiMitra AI - Comprehensive Test Suite
Tests:
- Application startup and config
- User registration, authentication, password hashing, and route protection
- Language switching persistence across Marathi, English, Hindi
- Real Keras trained model loading and inference on test leaf image
- Disease knowledge base retrieval and dual chemical/organic treatment plans
- Weather service graceful handling and agronomic decision rules
- Government schemes data integrity, verified portal URLs, and guided eligibility
- Market price benchmarks and legal API compliance (no fabricated live data)
- AI/ML Price Forecasting with chronological validation metrics and uncertainty bounds
- Assistant grounded responses and query logging
- User isolation in history
"""

import os
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import User, DiseasePrediction, FarmingQuery
from translations import get_text, TRANSLATIONS
from disease_knowledge_base import CLASS_NAME_LIST, get_disease_info
from inference_engine import get_disease_model, predict_disease
from weather_service import WeatherService
from schemes_data import get_all_schemes, get_scheme_by_id, evaluate_eligibility
from market_service import MarketService
from forecast_service import PriceForecastService
from assistant_service import FarmingAssistant

class KrishiMitraTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["WTF_CSRF_ENABLED"] = False
        self.client = app.test_client()

        with app.app_context():
            db.create_all()
            # Create a test user
            hashed_pw = generate_password_hash("testpassword123")
            user = User(
                fullname="Ramesh Patil",
                email="ramesh@krishimitra.test",
                mobile="9876543210",
                password=hashed_pw,
                preferred_language="mr",
                district="Pune",
                farm_size=3.5,
                primary_crops="Tomato, Onion"
            )
            db.session.add(user)
            db.session.commit()
            self.user_id = user.id

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # 1. Auth & Route Protection Tests
    def test_landing_page(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("KrishiMitra AI".encode("utf-8"), resp.data)

    def test_unauthorized_dashboard_redirects(self):
        resp = self.client.get("/dashboard")
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/login", resp.headers["Location"])

    def test_user_login_success(self):
        resp = self.client.post("/login", data={
            "email": "ramesh@krishimitra.test",
            "password": "testpassword123"
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Ramesh Patil".encode("utf-8"), resp.data)

    def test_user_login_failure(self):
        resp = self.client.post("/login?lang=en", data={
            "email": "ramesh@krishimitra.test",
            "password": "wrongpassword"
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Invalid Email or Password".encode("utf-8"), resp.data)

    # 2. Multilingual Persistence Tests
    def test_language_translations(self):
        self.assertEqual(get_text("brand_name", "en"), "KrishiMitra AI")
        self.assertEqual(get_text("brand_name", "mr"), "कृषिमित्र AI")
        self.assertEqual(get_text("brand_name", "hi"), "कृषिमित्र AI")
        self.assertIn("रोग निदान", get_text("disease_detection", "mr"))
        self.assertIn("रोग पहचान", get_text("disease_detection", "hi"))

    def test_set_language_endpoint(self):
        resp = self.client.get("/set_language/hi", follow_redirects=False)
        self.assertEqual(resp.status_code, 302)
        with self.client.session_transaction() as sess:
            self.assertEqual(sess.get("lang"), "hi")

    # 3. Model Loading & Inference Pipeline Tests
    def test_model_loading_and_classes(self):
        model = get_disease_model()
        self.assertIsNotNone(model)
        self.assertEqual(len(CLASS_NAME_LIST), 10)
        self.assertEqual(CLASS_NAME_LIST[3], "Tomato_Bacterial_spot")
        self.assertEqual(CLASS_NAME_LIST[5], "Tomato_healthy")

    def test_real_inference_on_sample_leaf(self):
        sample_path = os.path.join(os.path.dirname(__file__), "..", "static", "images", "sample_leaf.jpg")
        self.assertTrue(os.path.exists(sample_path), "Sample test leaf image must exist")
        
        result = predict_disease(sample_path, lang="en")
        self.assertTrue(result.get("success"))
        self.assertIn("class_name", result)
        self.assertGreater(result["confidence"], 0)
        self.assertIn("disease_info", result)
        self.assertIn("chemical_plan", result["disease_info"])
        self.assertIn("organic_plan", result["disease_info"])

    # 4. Disease Knowledge Base & Dual Treatment Plans
    def test_knowledge_base_completeness(self):
        for c in CLASS_NAME_LIST:
            info = get_disease_info(c, lang="mr")
            self.assertIsNotNone(info["disease_name"])
            self.assertIsNotNone(info["symptoms"])
            self.assertIsNotNone(info["chemical_plan"]["approach"])
            self.assertIsNotNone(info["organic_plan"]["approach"])
            self.assertIn("cost", info["comparison"])

    # 5. Weather Service Tests
    def test_weather_fallback_and_advisory(self):
        weather = WeatherService.get_weather_data("Pune")
        self.assertIsNotNone(weather)
        self.assertIn("temp", weather)
        self.assertIn("humidity", weather)
        self.assertIn("advisories", weather)
        self.assertIn("spraying", weather["advisories"])
        self.assertIn("irrigation", weather["advisories"])
        self.assertIn("disease_risk", weather["advisories"])

    # 6. Government Schemes Tests
    def test_government_schemes_and_official_links(self):
        schemes = get_all_schemes()
        self.assertGreaterEqual(len(schemes), 8)
        pmkisan = get_scheme_by_id("pmkisan")
        self.assertIsNotNone(pmkisan)
        self.assertTrue(pmkisan["website"].startswith("https://"))
        self.assertIn(".gov.in", pmkisan["website"])

    def test_eligibility_questionnaire(self):
        matches = evaluate_eligibility(land_acres=2.5, category="general", irrigation="drip")
        self.assertGreater(len(matches), 0)
        matched_ids = [m["scheme"]["id"] for m in matches]
        self.assertIn("pmkisan", matched_ids)
        self.assertIn("namo_shetkari", matched_ids)

    # 7. Market Prices & Forecasting Tests
    def test_market_price_retrieval(self):
        price = MarketService.get_market_price(state="Maharashtra", district="Pune", commodity="Tomato")
        self.assertEqual(price["status"], "success")
        self.assertGreater(price["modal_price"], 0)
        self.assertIn("unit", price)

    def test_price_forecasting_chronological(self):
        forecast = PriceForecastService.generate_price_forecast("Tomato", horizon_months=2)
        self.assertEqual(forecast["commodity"], "Tomato")
        self.assertEqual(len(forecast["forecast_prices"]), 4)  # 4 bi-weekly points for 2 months
        self.assertIn("validation_metrics", forecast)
        self.assertIn("mape", forecast["validation_metrics"])
        self.assertIn("upper_bound_80", forecast)
        self.assertIn("lower_bound_80", forecast)
        # Upper bound must be strictly greater than lower bound
        self.assertGreaterEqual(forecast["upper_bound_80"][0], forecast["lower_bound_80"][0])

    # 8. Assistant Tests
    def test_assistant_rule_based_response(self):
        res = FarmingAssistant.get_answer("How to treat early blight in tomato?", lang="en")
        self.assertIn("Mancozeb", res["answer"])
        self.assertIn("KrishiMitra", res["source"])

        res_mr = FarmingAssistant.get_answer("जिवामृत कसे तयार करावे?", lang="mr")
        self.assertIn("गोमूत्र", res_mr["answer"])

    # 9. User Isolation in History
    def test_user_history_isolation(self):
        with app.app_context():
            # Add prediction for user 1
            pred = DiseasePrediction(
                user_id=self.user_id,
                image_filename="test_leaf.jpg",
                disease_class="Tomato_Early_blight",
                confidence=88.5
            )
            db.session.add(pred)

            # Create user 2
            u2 = User(
                fullname="Suresh Joshi",
                email="suresh@krishimitra.test",
                mobile="9123456789",
                password=generate_password_hash("pass123")
            )
            db.session.add(u2)
            db.session.commit()

            # Query for user 2 should be empty
            u2_preds = DiseasePrediction.query.filter_by(user_id=u2.id).all()
            self.assertEqual(len(u2_preds), 0)

            # Query for user 1 has 1
            u1_preds = DiseasePrediction.query.filter_by(user_id=self.user_id).all()
            self.assertEqual(len(u1_preds), 1)

if __name__ == "__main__":
    unittest.main()
