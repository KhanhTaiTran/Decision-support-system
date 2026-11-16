"""Shared CSV fields and criterion direction. Keep UI and algorithm in sync."""

CRITERIA = {
    "monthly_cost_vnd": ("Total monthly cost (VND)", False),
    "distance_km": ("Distance to campus (km)", False),
    "area_m2": ("Floor area (m²)", True),
    "security_score": ("Security (1–5)", True),
    "amenities_score": ("Amenities (1–5)", True),
}
