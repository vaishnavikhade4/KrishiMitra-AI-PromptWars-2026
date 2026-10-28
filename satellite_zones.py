# -*- coding: utf-8 -*-
"""
KrishiMitra AI — Satellite Zone Analysis
==========================================
Divides a farm boundary into a configurable spatial grid,
computes per-zone NDVI statistics, detects anomalies, and
generates evidence-based inspection priority recommendations.

Anomaly detection rules (all configurable, rule-based — no ML):
  - Zone NDVI is more than 1.5 × std_dev below field mean → "inspect"
  - Zone has > 30% very_low pixels → "high-priority"
  - Zone NDVI declined > 0.15 vs previous analysis → "inspect"

Priority levels:
  "monitor"        — within normal range, no action required
  "inspect"        — below field average; field visit recommended
  "high-priority"  — significant concern; prompt inspection recommended
"""

import math
import json
import logging
from typing import Dict, Any, List, Tuple, Optional

import numpy as np

logger = logging.getLogger(__name__)

# Zone grid dimensions (can be overridden by caller)
DEFAULT_ZONE_ROWS = 3
DEFAULT_ZONE_COLS = 3

# Anomaly thresholds (configurable)
ANOMALY_STD_MULTIPLIER = 1.5   # Zone mean < field_mean - N*field_std → inspect
HIGH_PRIORITY_VERY_LOW_PCT = 30.0  # % of very-low pixels in zone → high-priority
HISTORICAL_DECLINE_THRESHOLD = 0.15  # NDVI drop vs previous observation → inspect


def _zone_label(row: int, col: int, n_cols: int) -> str:
    """Returns a human-readable zone identifier, e.g., A1, A2, B1, B3."""
    row_letter = chr(ord("A") + row)
    return f"{row_letter}{col + 1}"


def compute_zone_grid(
    ndvi_grid: np.ndarray,
    field_mask: np.ndarray,
    lon_steps: np.ndarray,
    lat_steps: np.ndarray,
    polygon: Dict,
    n_rows: int = DEFAULT_ZONE_ROWS,
    n_cols: int = DEFAULT_ZONE_COLS,
    field_mean: Optional[float] = None,
    field_std: Optional[float] = None,
    previous_zones: Optional[List[Dict]] = None,
) -> List[Dict]:
    """
    Divides the ndvi_grid into an n_rows × n_cols grid of rectangular zones,
    computes statistics per zone, detects anomalies, and returns a list of
    zone dicts suitable for JSON serialisation.

    Parameters
    ----------
    ndvi_grid      : 2D numpy array of NDVI values (NaN = no data)
    field_mask     : boolean 2D array — True for pixels inside field polygon
    lon_steps      : 1D array of longitude values for each column
    lat_steps      : 1D array of latitude values for each row
    polygon        : GeoJSON Polygon dict (for centroid calculation)
    n_rows, n_cols : zone grid dimensions
    field_mean     : pre-computed mean NDVI of entire field (or None to compute)
    field_std      : pre-computed std NDVI of entire field (or None to compute)
    previous_zones : list of zone dicts from a prior analysis for change detection

    Returns list of zone dicts with keys:
      id, label, center_lat, center_lon, bbox,
      ndvi_mean, ndvi_min, ndvi_max, ndvi_std,
      valid_pixel_pct, very_low_pct, distribution,
      priority, priority_reason, ndvi_change
    """
    grid_rows, grid_cols = ndvi_grid.shape

    # Compute field-level stats if not provided
    in_field = ndvi_grid[field_mask]
    valid_field = in_field[~np.isnan(in_field)]
    if field_mean is None:
        field_mean = float(np.nanmean(valid_field)) if len(valid_field) > 0 else 0.4
    if field_std is None:
        field_std = float(np.nanstd(valid_field)) if len(valid_field) > 0 else 0.1

    # Build previous zone NDVI lookup
    prev_lookup: Dict[str, float] = {}
    if previous_zones:
        for pz in previous_zones:
            if pz.get("ndvi_mean") is not None:
                prev_lookup[pz["label"]] = pz["ndvi_mean"]

    zones = []
    zone_id = 0

    for zr in range(n_rows):
        for zc in range(n_cols):
            zone_id += 1
            label = _zone_label(zr, zc, n_cols)

            # Row/col index ranges for this zone within the ndvi_grid
            r_start = int(zr * grid_rows / n_rows)
            r_end   = int((zr + 1) * grid_rows / n_rows)
            c_start = int(zc * grid_cols / n_cols)
            c_end   = int((zc + 1) * grid_cols / n_cols)

            # Slice zone
            zone_ndvi = ndvi_grid[r_start:r_end, c_start:c_end]
            zone_mask = field_mask[r_start:r_end, c_start:c_end]

            zone_in_field = zone_ndvi[zone_mask]
            valid_zone = zone_in_field[~np.isnan(zone_in_field)]

            total_zone_px = int(np.sum(zone_mask))
            valid_zone_px = len(valid_zone)
            valid_pct = round(100.0 * valid_zone_px / max(total_zone_px, 1), 1)

            # Zone centre
            zone_lats = lat_steps[r_start:r_end]
            zone_lons = lon_steps[c_start:c_end]
            center_lat = float(np.mean(zone_lats)) if len(zone_lats) > 0 else 0
            center_lon = float(np.mean(zone_lons)) if len(zone_lons) > 0 else 0

            # Zone bounding box
            bbox = {
                "south": round(float(zone_lats[0]), 6) if len(zone_lats) > 0 else 0,
                "north": round(float(zone_lats[-1]), 6) if len(zone_lats) > 0 else 0,
                "west":  round(float(zone_lons[0]), 6) if len(zone_lons) > 0 else 0,
                "east":  round(float(zone_lons[-1]), 6) if len(zone_lons) > 0 else 0,
            }

            if len(valid_zone) == 0:
                zones.append({
                    "id": zone_id,
                    "label": label,
                    "center_lat": round(center_lat, 6),
                    "center_lon": round(center_lon, 6),
                    "bbox": bbox,
                    "ndvi_mean": None,
                    "ndvi_min": None,
                    "ndvi_max": None,
                    "ndvi_std": None,
                    "valid_pixel_pct": valid_pct,
                    "very_low_pct": 0.0,
                    "distribution": {},
                    "priority": "monitor",
                    "priority_reason": "Insufficient valid data in this zone.",
                    "ndvi_change": None,
                })
                continue

            z_mean = float(np.nanmean(valid_zone))
            z_min  = float(np.nanmin(valid_zone))
            z_max  = float(np.nanmax(valid_zone))
            z_std  = float(np.nanstd(valid_zone))

            # Category distribution for zone
            dist = {"high": 0, "good": 0, "moderate": 0, "low": 0, "very_low": 0}
            for v in valid_zone:
                if v > 0.50:   dist["high"] += 1
                elif v > 0.35: dist["good"] += 1
                elif v > 0.20: dist["moderate"] += 1
                elif v > 0.05: dist["low"] += 1
                else:          dist["very_low"] += 1

            dist_pct = {k: round(100.0 * n / valid_zone_px, 1) for k, n in dist.items()}
            very_low_pct = dist_pct["very_low"]

            # Historical NDVI change
            ndvi_change = None
            if label in prev_lookup:
                ndvi_change = round(z_mean - prev_lookup[label], 4)

            # ── Anomaly / priority classification ──────────────────────────
            priority = "monitor"
            priority_reason = "Zone NDVI is within normal field variation."

            if very_low_pct >= HIGH_PRIORITY_VERY_LOW_PCT:
                priority = "high-priority"
                priority_reason = (
                    f"{very_low_pct:.0f}% of zone area shows very low NDVI (<0.05). "
                    "This may indicate bare soil, crop stress, or damaged vegetation. "
                    "Prompt field inspection is recommended."
                )
            elif field_std > 0 and z_mean < (field_mean - ANOMALY_STD_MULTIPLIER * field_std):
                priority = "inspect"
                diff = round(field_mean - z_mean, 3)
                priority_reason = (
                    f"Zone mean NDVI ({z_mean:.3f}) is {diff:.3f} below the field average "
                    f"({field_mean:.3f}). This zone shows lower vegetation signal relative to "
                    "the rest of the field. Inspect for possible stress, uneven growth, or bare patches."
                )
            elif ndvi_change is not None and ndvi_change < -HISTORICAL_DECLINE_THRESHOLD:
                priority = "inspect"
                priority_reason = (
                    f"Zone NDVI declined by {abs(ndvi_change):.3f} compared to the previous "
                    "observation. A significant decline may indicate crop stress, pest pressure, "
                    "or weather impact. Field inspection is recommended."
                )
            elif z_mean < 0.20:
                priority = "inspect"
                priority_reason = (
                    f"Zone mean NDVI ({z_mean:.3f}) is below the moderate threshold. "
                    "This may reflect early growth stage, soil exposure, or crop stress. "
                    "Monitor closely or inspect if conditions persist."
                )

            zones.append({
                "id": zone_id,
                "label": label,
                "center_lat": round(center_lat, 6),
                "center_lon": round(center_lon, 6),
                "bbox": bbox,
                "ndvi_mean": round(z_mean, 4),
                "ndvi_min": round(z_min, 4),
                "ndvi_max": round(z_max, 4),
                "ndvi_std": round(z_std, 4),
                "valid_pixel_pct": valid_pct,
                "very_low_pct": very_low_pct,
                "distribution": dist_pct,
                "priority": priority,
                "priority_reason": priority_reason,
                "ndvi_change": ndvi_change,
            })

    return zones


def summarise_anomalies(zones: List[Dict]) -> Dict[str, Any]:
    """
    Returns a compact summary of zone priorities.
    { "high_priority": [...labels], "inspect": [...labels], "monitor": [...labels],
      "total_zones": N, "alert_count": M }
    """
    high = [z["label"] for z in zones if z["priority"] == "high-priority"]
    inspect = [z["label"] for z in zones if z["priority"] == "inspect"]
    monitor = [z["label"] for z in zones if z["priority"] == "monitor"]

    return {
        "high_priority": high,
        "inspect": inspect,
        "monitor": monitor,
        "total_zones": len(zones),
        "alert_count": len(high) + len(inspect),
    }
