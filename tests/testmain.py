import unittest
from unittest.mock import patch
from GPScalc import (
    haversine_distance,
    find_closest_points,
    input_array
)

# ChatGPT-aided test cases
class TestGeoCalculations(unittest.TestCase):
    def test_haversine_distance(self):
        """
        Simple distance check: London (51.5074, -0.1278) to Paris (48.8566, 2.3522)
        is roughly 343 km. We allow ±5 km for rounding.
        """
        dist = haversine_distance(51.5074, -0.1278, 48.8566, 2.3522)
        self.assertAlmostEqual(dist, 343, delta=5)

    def test_find_closest_points(self):
        """
        Check that find_closest_points correctly identifies 
        the nearest reference point in array2 for each point in array1.
        """
        array1 = [(0, 0), (10, 10)]
        array2 = [(1, 1), (20, 20), (-1, -1)]

        results = find_closest_points(array1, array2)
        # results: a list of tuples of the form:
        #  ("Location A", (lat1, lon1), (closest_lat2, closest_lon2), distance)

        # For the first point (0,0), either (1,1) or (-1,-1) might be equally close,
        # but by iteration, we assume (1,1) is chosen first.
        self.assertEqual(results[0][2], (1, 1))

        # For the second point (10,10), the distance to (1,1) is less than (20,20) or (-1,-1).
        self.assertEqual(results[1][2], (1, 1))


class TestInputArray(unittest.TestCase):
    @patch("builtins.input", side_effect=[
        "2",                   # number of points for array
        "40.7128, -74.0060",   # first point (decimal)
        "48.8566, 2.3522",     # second point (decimal)
    ])
    def test_input_array_decimal(self, mock_input):
        """
        Mock user input to test input_array with decimal format ("1").
        """
        array = input_array("Test Array", "1")
        self.assertEqual(len(array), 2, "Should contain 2 points.")
        self.assertAlmostEqual(array[0][0], 40.7128, places=4)
        self.assertAlmostEqual(array[0][1], -74.0060, places=4)
        self.assertAlmostEqual(array[1][0], 48.8566, places=4)
        self.assertAlmostEqual(array[1][1], 2.3522, places=4)

    @patch("builtins.input", side_effect=[
        "1",              # number of points
        "40 44 54.36 73 59 8.36"  # 1 DMS point example
    ])
    def test_input_array_dms(self, mock_input):
        """
        Mock user input to test input_array with DMS format ("2").
        We'll just do 1 point for brevity.
        """
        array = input_array("Test Array", "2")
        self.assertEqual(len(array), 1, "Should contain 1 point.")

        # Convert DMS: lat => 40 + 44/60 + 54.36/3600 -> ~40.7484
        #              lon => 73 + 59/60 + 8.36/3600 -> ~73.9856
        lat, lon = array[0]
        self.assertAlmostEqual(lat, 40.7484, delta=0.001)
        self.assertAlmostEqual(lon, 73.9856, delta=0.001)


if __name__ == '__main__':
    unittest.main()