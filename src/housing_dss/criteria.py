"""Shared CSV fields and criterion direction. Keep UI and algorithm in sync."""

CRITERIA = {
    "monthly_cost_vnd": ("Total monthly cost (VND)", False),
    "distance_km": ("Distance to campus (km)", False),
    "area_m2": ("Floor area (m²)", True),
    "security_score": ("Security (1–5)", True),
    "amenities_score": ("Amenities (1–5)", True),
}

DEFAULT_WEIGHT = 20

PRESET_PROFILES : dict[str, dict[str, float]] = {
    "Balanced": {
        "monthly_cost_vnd": 20,
        "distance_km": 20,
        "area_m2": 20,
        "security_score": 20,
        "amenities_score": 20,
    },
    "Budget-First": {
        "monthly_cost_vnd": 60,
        "distance_km": 10,
        "area_m2": 10,
        "security_score": 10,
        "amenities_score": 10,
    },
    "Campus-Proximity": {
        "monthly_cost_vnd": 10,
        "distance_km": 60,
        "area_m2": 10,
        "security_score": 10,
        "amenities_score": 10,
    },
    "Comfort & Space": {
        "monthly_cost_vnd": 10,
        "distance_km": 10,
        "area_m2": 35,
        "security_score": 20,
        "amenities_score": 25,
    },
}

