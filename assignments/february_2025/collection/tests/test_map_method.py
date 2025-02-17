import unittest

from src.map_method import MapMethod


class MapMethodTest(unittest.TestCase):
    def setUp(self):
        self.map = MapMethod()

    def test_map_is_empty(self):
        self.assertTrue(self.map.is_empty())

    def test_map_adds_keys_and_values(self):
        self.map.put("first", "I love neutrals")
        self.map.put("second", "I love reading")
        self.assertEqual(self.map.size(), 2)

    def test_map_contains_value_returns_value(self):
        self.map.put("first", "I love neutrals")
        self.map.put("second", "I love reading")
        self.assertTrue(self.map.contains_value("I love neutrals"))
        self.assertFalse(self.map.contains_value("I love"))

    def test_map_contains_key_returns_correct_value(self):
        self.map.put("first", "I love neutrals")
        self.map.put("second", "I love reading")
        self.assertTrue(self.map.contains_key("first"))
        self.assertFalse(self.map.contains_key("third"))

    def test_map_get_method_returns_value_of_key(self):
        self.map.put("first", "I love neutrals")
        self.map.put("second", "I love reading")
        self.assertEqual(self.map.get("first"), "I love neutrals")

    def test_map_removes_key_and_value_and_return_value(self):
        self.map.put("first", "I love neutrals")
        self.map.put("second", "I love reading")
        self.assertEqual(self.map.remove("first"), "I love neutrals")
        self.assertIsNone(self.map.remove("yes"))

    def test_map_clears_all(self):
        self.map.put("first", "I love neutrals")
        self.map.put("second", "I love reading")
        self.map.clear()
        self.assertTrue(self.map.is_empty())

if __name__ == '__main__':
    unittest.main()