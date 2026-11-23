import unittest
from housing_dss.criteria import CRITERIA, PRESET_PROFILES
from housing_dss.topsis import rank_rooms

def room(id, cost : float = 100, distance : float = 1, area : float = 20, security : int =3, amenities : int = 3):
    return dict(id=id, monthly_cost_vnd=cost, distance_km=distance, area_m2=area,
                security_score=security, amenities_score=amenities)

class TopsisTests(unittest.TestCase):
    def setUp(self):
        self.weights: dict[str, float] = dict.fromkeys(CRITERIA, 1.0)

    def test_dominant_option_has_ideal_score(self):
        result = rank_rooms([room('B', 200, 2, 10, 1, 1), room('A', 100, 1, 20, 5, 5)], self.weights)
        self.assertEqual([r['id'] for r in result], ['A', 'B'])
        self.assertAlmostEqual(result[0]['score'], 1)
        self.assertAlmostEqual(result[1]['score'], 0)

    def test_identical_options_tie_and_sort_by_id(self):
        result = rank_rooms([room('B'), room('A')], self.weights)
        self.assertEqual([r['id'] for r in result], ['A', 'B'])
        self.assertTrue(all(r['score'] == 0.5 for r in result))

    def test_single_and_empty_candidate_sets(self):
        self.assertEqual(rank_rooms([], self.weights), [])
        self.assertEqual(rank_rooms([room('A')], self.weights)[0]['score'], 0.5)

    def test_zero_column_is_safe(self):
        result = rank_rooms([room('A', distance=0), room('B', distance=0)], self.weights)
        self.assertEqual(result[0]['score'], 0.5)

    def test_weights_change_ranking(self):
        rooms = [room('cheap', cost=100, area=10), room('large', cost=200, area=30)]
        cost_only: dict[str, float] = dict.fromkeys(CRITERIA, 0.0)
        cost_only['monthly_cost_vnd'] = 1.0
        area_only: dict[str, float] = dict.fromkeys(CRITERIA, 0.0)
        area_only['area_m2'] = 1.0
        self.assertEqual(rank_rooms(rooms, cost_only)[0]['id'], 'cheap')
        self.assertEqual(rank_rooms(rooms, area_only)[0]['id'], 'large')

    def test_invalid_weights_and_values(self):
        for weights in [dict.fromkeys(CRITERIA, 0), dict.fromkeys(CRITERIA, -1), dict.fromkeys(CRITERIA, float('nan'))]:
            with self.assertRaises(ValueError):
                rank_rooms([room('A')], weights)
        with self.assertRaises(ValueError):
            rank_rooms([room('A', cost=float('inf'))], self.weights)

    def test_preset_profiles_sensitivity(self):
        cheap_distant = room('cheap_distant', cost=1500000, distance=8.0, area=15, security=2, amenities=2)
        near_expensive = room('near_expensive', cost=4500000, distance=0.5, area=22, security=4, amenities=3)
        spacious_comfy = room('spacious_comfy', cost=3500000, distance=3.0, area=35, security=5, amenities=5)

        candidates = [cheap_distant, near_expensive, spacious_comfy]

        budget_rank = rank_rooms(candidates, PRESET_PROFILES['Budget-First'])
        self.assertEqual(budget_rank[0]['id'], 'cheap_distant')

        campus_rank = rank_rooms(candidates, PRESET_PROFILES['Campus-Proximity'])
        self.assertEqual(campus_rank[0]['id'], 'near_expensive')

        comfort_rank = rank_rooms(candidates, PRESET_PROFILES['Comfort & Space'])
        self.assertEqual(comfort_rank[0]['id'], 'spacious_comfy')


if __name__ == '__main__':
    unittest.main()
