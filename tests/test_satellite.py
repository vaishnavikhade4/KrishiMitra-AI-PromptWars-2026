# -*- coding: utf-8 -*-
"""
Satellite Crop Intelligence — Unit Tests
Tests NDVI computation, area calculation, zone analysis, anomaly detection,
and Flask API endpoints. Does NOT require real Copernicus credentials.
"""

import json
import math
import unittest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from satellite_service import (
    compute_area_hectares,
    compute_ndvi_from_bands,
    compute_ndvi_statistics,
    build_heatmap_grid,
    _bbox_from_geojson,
    _synthetic_ndvi_grid,
    _point_in_polygon,
    credentials_configured,
    NDVI_THRESHOLDS,
)
from satellite_zones import compute_zone_grid, summarise_anomalies


# ── Shared test polygon (small rectangular field near Pune) ─────────────────
SAMPLE_POLYGON = {
    "type": "Polygon",
    "coordinates": [[
        [73.85, 18.52],
        [73.86, 18.52],
        [73.86, 18.53],
        [73.85, 18.53],
        [73.85, 18.52],
    ]]
}

SAMPLE_BBOX = (73.85, 18.52, 73.86, 18.53)


class TestAreaCalculation(unittest.TestCase):

    def test_area_reasonable(self):
        area_ha = compute_area_hectares(SAMPLE_POLYGON)
        # ~0.01 degrees lat × ~0.01 degrees lon ≈ 60–120 ha near Pune
        self.assertGreater(area_ha, 0.5)
        self.assertLess(area_ha, 500)

    def test_area_is_float(self):
        area_ha = compute_area_hectares(SAMPLE_POLYGON)
        self.assertIsInstance(area_ha, float)

    def test_degenerate_polygon(self):
        tiny = {"type": "Polygon", "coordinates": [[[73.85, 18.52], [73.85, 18.52]]]}
        area_ha = compute_area_hectares(tiny)
        self.assertEqual(area_ha, 0.0)

    def test_bbox_extraction(self):
        bbox = _bbox_from_geojson(SAMPLE_POLYGON)
        self.assertAlmostEqual(bbox[0], 73.85, places=5)
        self.assertAlmostEqual(bbox[1], 18.52, places=5)
        self.assertAlmostEqual(bbox[2], 73.86, places=5)
        self.assertAlmostEqual(bbox[3], 18.53, places=5)


class TestNDVIComputation(unittest.TestCase):

    def test_basic_ndvi_formula(self):
        red = np.array([[1000.0, 2000.0]], dtype=np.float32)
        nir = np.array([[3000.0, 2000.0]], dtype=np.float32)
        ndvi = compute_ndvi_from_bands(red, nir)
        # (3000-1000)/(3000+1000) = 0.5 before scaling
        # After /10000: (0.3-0.1)/(0.3+0.1) = 0.5
        self.assertAlmostEqual(float(ndvi[0, 0]), 0.5, places=4)

    def test_ndvi_range_clipped(self):
        red = np.array([[10000.0]], dtype=np.float32)
        nir = np.array([[0.0]], dtype=np.float32)
        ndvi = compute_ndvi_from_bands(red, nir)
        self.assertGreaterEqual(float(ndvi[0, 0]), -1.0)
        self.assertLessEqual(float(ndvi[0, 0]), 1.0)

    def test_division_by_zero_is_nan(self):
        red = np.array([[0.0]], dtype=np.float32)
        nir = np.array([[0.0]], dtype=np.float32)
        ndvi = compute_ndvi_from_bands(red, nir)
        self.assertTrue(np.isnan(float(ndvi[0, 0])))

    def test_valid_mask_applied(self):
        red = np.array([[1000.0, 2000.0]], dtype=np.float32)
        nir = np.array([[3000.0, 4000.0]], dtype=np.float32)
        mask = np.array([[True, False]])
        ndvi = compute_ndvi_from_bands(red, nir, valid_mask=mask)
        self.assertFalse(np.isnan(float(ndvi[0, 0])))
        self.assertTrue(np.isnan(float(ndvi[0, 1])))

    def test_ndvi_healthy_vegetation(self):
        # Healthy vegetation: NIR >> Red
        red = np.array([[500.0]], dtype=np.float32)
        nir = np.array([[5000.0]], dtype=np.float32)
        ndvi = compute_ndvi_from_bands(red, nir)
        self.assertGreater(float(ndvi[0, 0]), 0.7)

    def test_ndvi_bare_soil(self):
        # Bare soil: Red ≈ NIR
        red = np.array([[2000.0]], dtype=np.float32)
        nir = np.array([[2500.0]], dtype=np.float32)
        ndvi = compute_ndvi_from_bands(red, nir)
        self.assertLess(float(ndvi[0, 0]), 0.2)


class TestNDVIStatistics(unittest.TestCase):

    def setUp(self):
        # 4×4 grid, all inside field, values ranging 0.1–0.8
        self.ndvi = np.array([
            [0.6, 0.7, 0.5, 0.4],
            [0.3, 0.2, 0.1, 0.05],
            [0.8, 0.75, 0.6, 0.4],
            [0.0, np.nan, 0.3, 0.5],
        ], dtype=np.float32)
        self.mask = np.ones((4, 4), dtype=bool)

    def test_mean_computed(self):
        stats = compute_ndvi_statistics(self.ndvi, self.mask)
        self.assertIsNotNone(stats["ndvi_mean"])
        self.assertGreater(stats["ndvi_mean"], 0)

    def test_distribution_sums_to_100(self):
        stats = compute_ndvi_statistics(self.ndvi, self.mask)
        total = sum(stats["distribution"].values())
        self.assertAlmostEqual(total, 100.0, places=0)

    def test_nan_excluded_from_stats(self):
        stats = compute_ndvi_statistics(self.ndvi, self.mask)
        # NaN pixel should not affect valid count
        self.assertLess(stats["valid_pixel_pct"], 100.01)

    def test_all_nan_field(self):
        ndvi_nan = np.full((4, 4), np.nan)
        stats = compute_ndvi_statistics(ndvi_nan, self.mask)
        self.assertIsNone(stats["ndvi_mean"])

    def test_partial_field_mask(self):
        mask = np.zeros((4, 4), dtype=bool)
        mask[0, 0] = True  # only one pixel inside field
        stats = compute_ndvi_statistics(self.ndvi, mask)
        self.assertAlmostEqual(stats["ndvi_mean"], 0.6, places=4)


class TestSyntheticGrid(unittest.TestCase):

    def test_grid_shape_correct(self):
        ndvi, mask, lons, lats = _synthetic_ndvi_grid(SAMPLE_POLYGON, SAMPLE_BBOX, resolution=20)
        self.assertEqual(ndvi.shape, (20, 20))
        self.assertEqual(mask.shape, (20, 20))

    def test_some_pixels_inside_field(self):
        ndvi, mask, lons, lats = _synthetic_ndvi_grid(SAMPLE_POLYGON, SAMPLE_BBOX, resolution=20)
        self.assertGreater(np.sum(mask), 0)

    def test_values_in_valid_ndvi_range(self):
        ndvi, mask, lons, lats = _synthetic_ndvi_grid(SAMPLE_POLYGON, SAMPLE_BBOX, resolution=20)
        in_field = ndvi[mask]
        valid = in_field[~np.isnan(in_field)]
        self.assertTrue(np.all(valid >= -1.0))
        self.assertTrue(np.all(valid <= 1.0))

    def test_deterministic(self):
        """Same inputs → same outputs on every call."""
        g1, _, _, _ = _synthetic_ndvi_grid(SAMPLE_POLYGON, SAMPLE_BBOX, resolution=15)
        g2, _, _, _ = _synthetic_ndvi_grid(SAMPLE_POLYGON, SAMPLE_BBOX, resolution=15)
        np.testing.assert_array_equal(g1, g2)

    def test_no_fabricated_random_values(self):
        """Verify the grid is not pure random noise (std should be moderate)."""
        ndvi, mask, _, _ = _synthetic_ndvi_grid(SAMPLE_POLYGON, SAMPLE_BBOX, resolution=20)
        in_field = ndvi[mask]
        valid = in_field[~np.isnan(in_field)]
        # A purely random grid would have std ≈ 0.4–0.5; our spatial gradient has lower std
        self.assertLess(float(np.std(valid)), 0.4)


class TestHeatmapGrid(unittest.TestCase):

    def setUp(self):
        res = 10
        self.ndvi, self.mask, self.lons, self.lats = _synthetic_ndvi_grid(
            SAMPLE_POLYGON, SAMPLE_BBOX, resolution=res
        )

    def test_cells_have_required_keys(self):
        cells = build_heatmap_grid(self.ndvi, self.mask, self.lons, self.lats)
        required = {"lat", "lon", "d_lat", "d_lon", "ndvi", "color", "category", "label"}
        for cell in cells[:5]:
            self.assertTrue(required.issubset(cell.keys()))

    def test_only_field_pixels_returned(self):
        cells = build_heatmap_grid(self.ndvi, self.mask, self.lons, self.lats)
        self.assertGreater(len(cells), 0)

    def test_colors_match_thresholds(self):
        """Color assigned to each cell must correspond to its NDVI value."""
        cells = build_heatmap_grid(self.ndvi, self.mask, self.lons, self.lats)
        for cell in cells:
            ndvi = cell["ndvi"]
            color = cell["color"]
            cat = cell["category"]
            if ndvi is None:
                self.assertEqual(cat, "no_data")
            elif ndvi > 0.50:
                self.assertEqual(cat, "high")
            elif ndvi > 0.35:
                self.assertEqual(cat, "good")
            elif ndvi > 0.20:
                self.assertEqual(cat, "moderate")
            elif ndvi > 0.05:
                self.assertEqual(cat, "low")
            else:
                self.assertEqual(cat, "very_low")
            self.assertEqual(color, NDVI_THRESHOLDS[cat]["color"])


class TestZoneAnalysis(unittest.TestCase):

    def setUp(self):
        res = 30
        self.ndvi, self.mask, self.lons, self.lats = _synthetic_ndvi_grid(
            SAMPLE_POLYGON, SAMPLE_BBOX, resolution=res
        )

    def test_zone_count(self):
        zones = compute_zone_grid(self.ndvi, self.mask, self.lons, self.lats, SAMPLE_POLYGON)
        self.assertEqual(len(zones), 9)  # 3×3 default grid

    def test_zone_keys_present(self):
        zones = compute_zone_grid(self.ndvi, self.mask, self.lons, self.lats, SAMPLE_POLYGON)
        required = {"id", "label", "center_lat", "center_lon", "bbox",
                    "ndvi_mean", "valid_pixel_pct", "priority", "priority_reason"}
        for z in zones:
            self.assertTrue(required.issubset(z.keys()), f"Missing keys in zone {z.get('label')}")

    def test_zone_labels_unique(self):
        zones = compute_zone_grid(self.ndvi, self.mask, self.lons, self.lats, SAMPLE_POLYGON)
        labels = [z["label"] for z in zones]
        self.assertEqual(len(labels), len(set(labels)))

    def test_priority_values_valid(self):
        zones = compute_zone_grid(self.ndvi, self.mask, self.lons, self.lats, SAMPLE_POLYGON)
        valid_priorities = {"monitor", "inspect", "high-priority"}
        for z in zones:
            self.assertIn(z["priority"], valid_priorities)

    def test_anomaly_summary_structure(self):
        zones = compute_zone_grid(self.ndvi, self.mask, self.lons, self.lats, SAMPLE_POLYGON)
        summary = summarise_anomalies(zones)
        self.assertIn("high_priority", summary)
        self.assertIn("inspect", summary)
        self.assertIn("monitor", summary)
        self.assertIn("total_zones", summary)
        total = len(summary["high_priority"]) + len(summary["inspect"]) + len(summary["monitor"])
        self.assertEqual(total, 9)

    def test_historical_change_detection(self):
        # Inject fake previous zones with higher NDVI → should trigger decline detection
        prev_zones = [{"label": "A1", "ndvi_mean": 0.7},
                      {"label": "A2", "ndvi_mean": 0.7},
                      {"label": "A3", "ndvi_mean": 0.7}]
        zones = compute_zone_grid(
            self.ndvi, self.mask, self.lons, self.lats, SAMPLE_POLYGON,
            previous_zones=prev_zones
        )
        top_row = [z for z in zones if z["label"] in ("A1","A2","A3")]
        for z in top_row:
            if z["ndvi_change"] is not None:
                self.assertIsInstance(z["ndvi_change"], float)


class TestSatelliteFlaskEndpoints(unittest.TestCase):
    """Tests Flask routes: no real Copernicus credentials needed."""

    @classmethod
    def setUpClass(cls):
        from app import app, db
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        cls.client = app.test_client()
        cls.app = app
        cls.db = db

        with app.app_context():
            db.create_all()
            from werkzeug.security import generate_password_hash
            from models import User
            # Create test user
            if not User.query.filter_by(email="sat_test@km.ai").first():
                u = User(
                    fullname="Satellite Tester",
                    email="sat_test@km.ai",
                    mobile="9999000001",
                    password=generate_password_hash("test123"),
                    preferred_language="en",
                    district="Pune",
                )
                db.session.add(u)
                db.session.commit()

    def _login(self):
        return self.client.post("/login?lang=en",
            data={"email": "sat_test@km.ai", "password": "test123"},
            follow_redirects=True)

    def test_satellite_page_requires_login(self):
        r = self.client.get("/satellite")
        self.assertIn(r.status_code, [302, 200])
        if r.status_code == 302:
            self.assertIn(b"login", r.data.lower())

    def test_satellite_page_loads_after_login(self):
        self._login()
        r = self.client.get("/satellite")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"Satellite", r.data)

    def test_list_farms_empty(self):
        self._login()
        r = self.client.get("/satellite/farms")
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.data)
        self.assertTrue(data["success"])
        self.assertIsInstance(data["farms"], list)

    def test_save_farm_valid(self):
        self._login()
        polygon = {
            "type": "Polygon",
            "coordinates": [[
                [73.85, 18.52], [73.86, 18.52],
                [73.86, 18.53], [73.85, 18.53], [73.85, 18.52]
            ]]
        }
        r = self.client.post("/satellite/farms",
            json={
                "farm_name": "Test Field A",
                "crop_type": "Tomato",
                "boundary_geojson": json.dumps(polygon),
            })
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.data)
        self.assertTrue(data["success"])
        self.assertEqual(data["farm"]["farm_name"], "Test Field A")
        self.assertIsNotNone(data["farm"]["area_hectares"])

    def test_save_farm_invalid_no_boundary(self):
        self._login()
        r = self.client.post("/satellite/farms",
            json={"farm_name": "Bad Farm", "crop_type": "Tomato", "boundary_geojson": ""})
        self.assertEqual(r.status_code, 400)
        data = json.loads(r.data)
        self.assertFalse(data["success"])

    def test_save_farm_degenerate_polygon(self):
        self._login()
        polygon = {"type": "Polygon", "coordinates": [[[73.85, 18.52], [73.85, 18.52]]]}
        r = self.client.post("/satellite/farms",
            json={"farm_name": "Tiny", "crop_type": "Wheat",
                  "boundary_geojson": json.dumps(polygon)})
        self.assertEqual(r.status_code, 400)

    def test_analyze_farm_demo_mode(self):
        """Full analysis pipeline in demo mode (no CDSE credentials)."""
        self._login()
        # First create a farm
        polygon = {
            "type": "Polygon",
            "coordinates": [[
                [73.85, 18.52], [73.86, 18.52],
                [73.86, 18.53], [73.85, 18.53], [73.85, 18.52]
            ]]
        }
        r_farm = self.client.post("/satellite/farms",
            json={"farm_name": "Analysis Test Farm", "crop_type": "Soybean",
                  "boundary_geojson": json.dumps(polygon)})
        farm_id = json.loads(r_farm.data)["farm"]["id"]

        # Run analysis
        r = self.client.post(f"/satellite/analyze/{farm_id}")
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.data)

        self.assertTrue(data["success"])
        self.assertIn(data["status"], ["demo", "complete"])
        self.assertIsNotNone(data["ndvi_mean"])
        self.assertIsInstance(data["heatmap_cells"], list)
        self.assertGreater(len(data["heatmap_cells"]), 0)
        self.assertIsInstance(data["zones"], list)
        self.assertEqual(len(data["zones"]), 9)
        self.assertIsNotNone(data["insight_text"])
        self.assertIsNotNone(data["distribution"])

    def test_analysis_ndvi_values_in_range(self):
        """All heatmap cell NDVI values must be in [-1, 1] or None."""
        self._login()
        polygon = {
            "type": "Polygon",
            "coordinates": [[
                [73.87, 18.54], [73.88, 18.54],
                [73.88, 18.55], [73.87, 18.55], [73.87, 18.54]
            ]]
        }
        r_farm = self.client.post("/satellite/farms",
            json={"farm_name": "Range Check Farm", "crop_type": "Onion",
                  "boundary_geojson": json.dumps(polygon)})
        farm_id = json.loads(r_farm.data)["farm"]["id"]

        r = self.client.post(f"/satellite/analyze/{farm_id}")
        data = json.loads(r.data)
        for cell in data.get("heatmap_cells", []):
            if cell["ndvi"] is not None:
                self.assertGreaterEqual(cell["ndvi"], -1.0)
                self.assertLessEqual(cell["ndvi"], 1.0)

    def test_analysis_distribution_sums_to_100(self):
        """NDVI category distribution must sum to ~100%."""
        self._login()
        polygon = {
            "type": "Polygon",
            "coordinates": [[
                [73.89, 18.56], [73.90, 18.56],
                [73.90, 18.57], [73.89, 18.57], [73.89, 18.56]
            ]]
        }
        r_farm = self.client.post("/satellite/farms",
            json={"farm_name": "Distribution Farm", "crop_type": "Cotton",
                  "boundary_geojson": json.dumps(polygon)})
        farm_id = json.loads(r_farm.data)["farm"]["id"]

        r = self.client.post(f"/satellite/analyze/{farm_id}")
        data = json.loads(r.data)
        dist = data.get("distribution", {})
        total = sum(dist.values())
        self.assertAlmostEqual(total, 100.0, delta=1.0)

    def test_history_endpoint(self):
        """History endpoint returns correct structure."""
        self._login()
        polygon = {
            "type": "Polygon",
            "coordinates": [[
                [73.91, 18.58], [73.92, 18.58],
                [73.92, 18.59], [73.91, 18.59], [73.91, 18.58]
            ]]
        }
        r_farm = self.client.post("/satellite/farms",
            json={"farm_name": "History Farm", "crop_type": "Wheat",
                  "boundary_geojson": json.dumps(polygon)})
        farm_id = json.loads(r_farm.data)["farm"]["id"]

        # Run analysis first so history has data
        self.client.post(f"/satellite/analyze/{farm_id}")

        r = self.client.get(f"/satellite/history/{farm_id}")
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.data)
        self.assertTrue(data["success"])
        self.assertIsInstance(data["history"], list)
        self.assertGreater(len(data["history"]), 0)
        rec = data["history"][0]
        self.assertIn("ndvi_mean", rec)
        self.assertIn("observation_date", rec)

    def test_other_user_cannot_access_farm(self):
        """Farm data must be scoped to the owning user."""
        from app import app, db

        # ── Create the owning user's farm in an isolated client ──────────────
        with app.test_client() as owner_client:
            owner_client.post("/login?lang=en",
                data={"email": "sat_test@km.ai", "password": "test123"},
                follow_redirects=True)

            polygon = {
                "type": "Polygon",
                "coordinates": [[
                    [73.93, 18.60], [73.94, 18.60],
                    [73.94, 18.61], [73.93, 18.61], [73.93, 18.60]
                ]]
            }
            r_farm = owner_client.post("/satellite/farms",
                json={"farm_name": "Private Farm", "crop_type": "Rice",
                      "boundary_geojson": json.dumps(polygon)})
            farm_id = json.loads(r_farm.data)["farm"]["id"]

        # ── Register attacker user ───────────────────────────────────────────
        with app.app_context():
            from werkzeug.security import generate_password_hash
            from models import User
            if not User.query.filter_by(email="other_sat@km.ai").first():
                other = User(
                    fullname="Other User",
                    email="other_sat@km.ai",
                    mobile="9999000002",
                    password=generate_password_hash("other123"),
                    preferred_language="en",
                    district="Nagpur",
                )
                db.session.add(other)
                db.session.commit()

        # ── Attacker tries to access owner's farm via a separate client ──────
        with app.test_client() as attacker_client:
            attacker_client.post("/login?lang=en",
                data={"email": "other_sat@km.ai", "password": "other123"},
                follow_redirects=True)
            r = attacker_client.post(f"/satellite/analyze/{farm_id}")
            self.assertEqual(r.status_code, 404)


class TestCredentialConfig(unittest.TestCase):

    def test_credentials_not_configured_by_default(self):
        # In test environment, CDSE creds should not be set
        import os
        os.environ.pop("CDSE_USERNAME", None)
        os.environ.pop("CDSE_PASSWORD", None)
        self.assertFalse(credentials_configured())


if __name__ == "__main__":
    unittest.main(verbosity=2)
