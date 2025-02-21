import unittest

from src.set_method import SetMethod

class SetMethodTest(unittest.TestCase):
    def setUp(self):
        self.set_method = SetMethod()

    def test_set_is_empty(self):
        self.assertTrue(self.set_method.is_empty())

    def test_set_add_items(self):
        self.set_method.add("firstExample")
        self.set_method.add("secondExample")
        self.assertEqual(self.set_method.size(), 2)

    def test_set_add_duplicates(self):
        self.set_method.add("firstExample")
        self.set_method.add("secondExample")
        with self.assertRaises(ValueError):
            self.set_method.add("firstExample")

    def test_set_remove_item(self):
        self.set_method.add("firstExample")
        self.set_method.add("secondExample")
        self.set_method.remove("firstExample")
        self.assertEqual(self.set_method.size(), 1)

    def test_set_contains_item(self):
        self.set_method.add("firstExample")
        self.set_method.add("secondExample")
        self.assertTrue(self.set_method.contains("firstExample"))
        self.assertFalse(self.set_method.contains("thirdExample"))

    def test_set_clear(self):
        self.set_method.add("firstExample")
        self.set_method.add("secondExample")
        self.set_method.clear()
        self.assertTrue(self.set_method.is_empty())

if __name__ == '__main__':
    unittest.main()