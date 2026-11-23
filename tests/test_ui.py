import unittest

from housing_dss.ui.results import format_rooms


class ResultFormattingTests(unittest.TestCase):
    def test_format_rooms_uses_display_labels_and_rounds_score(self):
        room = {
            "id": "R01",
            "name": "Maple Studio",
            "monthly_cost_vnd": 2500000.0,
            "distance_km": 4.5,
            "area_m2": 18.0,
            "security_score": 3.0,
            "amenities_score": 3.0,
            "score": 0.123456,
        }

        self.assertEqual(
            format_rooms([room]),
            [
                {
                    "ID": "R01",
                    "Room": "Maple Studio",
                    "Total monthly cost (VND)": 2500000.0,
                    "Distance to campus (km)": 4.5,
                    "Floor area (m²)": 18.0,
                    "Security (1–5)": 3.0,
                    "Amenities (1–5)": 3.0,
                    "TOPSIS score": 0.1235,
                }
            ],
        )
