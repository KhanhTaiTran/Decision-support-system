import unittest
from pathlib import Path
from streamlit.testing.v1 import AppTest

from housing_dss.criteria import CRITERIA, PRESET_PROFILES
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


class PresetProfileTests(unittest.TestCase):
    def test_preset_profiles_contain_expected_names_and_criteria(self):
        expected_profiles = {"Balanced", "Budget-First", "Campus-Proximity", "Comfort & Space"}
        self.assertEqual(set(PRESET_PROFILES.keys()), expected_profiles)

        for name, profile in PRESET_PROFILES.items():
            self.assertEqual(set(profile.keys()), set(CRITERIA.keys()))
            self.assertEqual(sum(profile.values()), 100, f"{name} weights must sum to 100")
            for crit, val in profile.items():
                self.assertGreaterEqual(val, 0, f"{name}[{crit}] must be non-negative")

    def test_sidebar_preset_buttons_update_sliders(self):
        app_path = Path(__file__).parent.parent / "app.py"
        at = AppTest.from_file(str(app_path))
        at.run()
        self.assertFalse(at.exception)

        # Default weights
        for key in CRITERIA:
            self.assertEqual(at.sidebar.slider(key=key).value, 20)

        # Click Budget-First
        at.sidebar.button(key="preset_budget_first").click().run()
        self.assertFalse(at.exception)
        for key, expected_val in PRESET_PROFILES["Budget-First"].items():
            self.assertEqual(at.sidebar.slider(key=key).value, expected_val)

        # Click Campus-Proximity
        at.sidebar.button(key="preset_campus_proximity").click().run()
        self.assertFalse(at.exception)
        for key, expected_val in PRESET_PROFILES["Campus-Proximity"].items():
            self.assertEqual(at.sidebar.slider(key=key).value, expected_val)

        # Click Comfort & Space
        at.sidebar.button(key="preset_comfort_space").click().run()
        self.assertFalse(at.exception)
        for key, expected_val in PRESET_PROFILES["Comfort & Space"].items():
            self.assertEqual(at.sidebar.slider(key=key).value, expected_val)

        # Click Balanced
        at.sidebar.button(key="preset_balanced").click().run()
        self.assertFalse(at.exception)
        for key, expected_val in PRESET_PROFILES["Balanced"].items():
            self.assertEqual(at.sidebar.slider(key=key).value, expected_val)

