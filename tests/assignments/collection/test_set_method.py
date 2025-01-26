import unittest
from assignments.collection.set_method import SetMethod


class SetMethodTest(unittest.TestCase):
    def setUp(self):
        self.set = SetMethod()

    def test_set_is_empty(self):
        self.assertTrue(self.set.is_empty())

    def test_set_add_XY_to_set(self):
        self.set.add("firstExample")
        self.set.add("secondExample")
        self.assertEqual(self.set.size(), 2)

    def test_set_add_XY_to_set_when_empty(self):
        self.assertTrue(self.set.is_empty())
        self.set.add("firstExample")
        self.set.add("secondExample")
        self.assertEqual(self.set.size(), 2)
        self.assertFalse(self.set.is_empty())

    def test_set_throws_exception_when_duplicates_are_found(self):
        self.set.add("firstExample")
        self.set.add("secondExample")
        self.set.add("thirdExample")
        self.set.add("fourthExample")
        with self.assertRaises(ValueError):
            self.set.add("firstExample")

    def test_set_add_no_duplicates_and_size_is_the_same(self):
        self.set.add("firstExample")
        self.set.add("secondExample")
        self.set.add("thirdExample")
        self.set.add("fourthExample")
        with self.assertRaises(ValueError):
            self.set.add("firstExample")
        self.assertEqual(self.set.size(), 4)

    def test_set_add_does_not_add_null(self):
        with self.assertRaises(ValueError):
            self.set.add(None)

    def test_set_remove_X_from_set(self):
        self.set.add("firstExample")
        self.set.add("secondExample")
        self.set.add("thirdExample")
        self.set.remove("secondExample")
        self.assertEqual(self.set.size(), 2)

    def test_set_does_not_remove_when_empty(self):
        self.assertTrue(self.set.is_empty())
        with self.assertRaises(ValueError):
            self.set.remove("example")

    def test_set_remove_throws_exception_when_element_does_not_exist(self):
        self.set.add("firstExample")
        self.set.add("secondExample")
        with self.assertRaises(ValueError):
            self.set.remove("example")

    def test_set_clears(self):
        self.set.add("firstExample")
        self.set.add("secondExample")
        self.set.add("thirdExample")
        self.set.clear()
        self.assertTrue(self.set.is_empty())
        self.assertEqual(self.set.size(), 0)

    def test_set_contains_X_from_set(self):
        self.set.add("firstExample")
        self.set.add("secondExample")
        self.assertTrue(self.set.contains("firstExample"))

    def test_set_does_not_contain_X(self):
        self.set.add("firstExample")
        self.set.add("secondExample")
        self.assertFalse(self.set.contains("thirdExample"))


if __name__ == '__main__':
    unittest.main()
