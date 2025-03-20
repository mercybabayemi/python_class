import unittest
from geo_political_zones import GeoPoliticalZONES
class TestGeoPoliticalZones(unittest.TestCase):

    def test_EnumValues(self):
        self.assertEqual(GeoPoliticalZONES.NORTH_WEST,GeoPoliticalZONES.get_state(self, "ogun"))

if __name__ == '__main__':
    unittest.main()
