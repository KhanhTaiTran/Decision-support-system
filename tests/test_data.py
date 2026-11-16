from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from housing_dss.data import load_rooms

class DataTests(unittest.TestCase):
    def test_sample_loads(self):
        rooms = load_rooms(Path(__file__).resolve().parents[1] / 'data' / 'rooms_sample.csv')
        self.assertEqual(len(rooms), 8)
        self.assertTrue(all(room['source'] == 'synthetic' for room in rooms))

    def test_duplicate_id_rejected(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / 'rooms.csv'
            path.write_text('id,name,source,monthly_cost_vnd,distance_km,area_m2,security_score,amenities_score\n'
                            'A,Room,synthetic,100,1,20,3,3\nA,Room,synthetic,200,2,30,4,4\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'duplicate ID'):
                load_rooms(path)
