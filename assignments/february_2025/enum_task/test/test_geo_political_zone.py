import unittest

from geo_political_zone import GeoPoliticalZONES


class TestZones(unittest.TestCase):
    def test_value_output(self):
        self.assertEqual(GeoPoliticalZONES.NORTH_WEST, GeoPoliticalZONES.NORTH_WEST)

    def test_get_state(self):
        self.assertEqual(GeoPoliticalZONES.SOUTH_WEST, GeoPoliticalZONES.get_state(self, "Ogun"))
        self.assertIsNone(GeoPoliticalZONES.get_state(self,"State"))

    def test_state_in_zone(self):
        self.assertTrue(GeoPoliticalZONES.get_state(self, "Kaduna"))
        self.assertFalse(GeoPoliticalZONES.get_state(self, "Gone"))


if __name__ == '__main__':
    unittest.main()
