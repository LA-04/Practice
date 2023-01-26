import unittest
from create_def import get_score

class TestCreateDef(unittest.TestCase):
    def test_allow_score(self):
        game_stamps = {{'offset': 0, 'score': {'home': 0, 'away': 0}},
                       {'offset': 16057, 'score': {'home': 1, 'away': 0}},
                       {'offset': 42029, 'score': {'home': 1, 'away': 1}},
                       {'offset': 99792, 'score': {'home': 1, 'away': 2}},
                       {'offset': 99983, 'score': {'home': 1, 'away': 2}}}
        offset = 99900

        expected_result = (1,2)

        self.assertEqual(get_score(game_stamps, offset), (1,2))