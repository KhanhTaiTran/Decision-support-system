"""Shared CSV fields and criterion direction. Keep UI and algorithm in sync."""

CRITERIA = {
    "monthly_cost_vnd": ("Tổng chi phí tháng (VND)", False),
    "distance_km": ("Khoảng cách tới trường (km)", False),
    "area_m2": ("Diện tích (m²)", True),
    "security_score": ("An ninh (1–5)", True),
    "amenities_score": ("Tiện nghi (1–5)", True),
}
