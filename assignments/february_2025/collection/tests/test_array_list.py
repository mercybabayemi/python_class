import unittest

from src.array_list import ArrayListMethod

class TestArrayListMethod(unittest.TestCase):
    def setUp(self):
        self.list = ArrayListMethod()

    def test_list_is_empty(self):
        self.assertTrue(self.list.is_empty())

    def test_add_item(self):
        self.list.add("firstExample")
        self.assertEqual(self.list.get(0), "firstExample")

    def test_add_item_at_index(self):
        self.list.add("firstExample")
        self.list.add("secondExample")
        self.list.add_at_index(1, "replacementExample")
        self.assertEqual(self.list.get(1), "replacementExample")
        self.assertEqual(len(self.list), 3)

    def test_add_item_throws_exception_when_none(self):
        with self.assertRaises(ValueError):
            self.list.add(None)

    def test_add_item_at_index_throws_exception_when_none(self):
        self.list.add("firstExample")
        with self.assertRaises(ValueError):
            self.list.add_at_index(1, None)

    def test_remove_element(self):
        self.list.add("firstExample")
        self.list.add("secondExample")
        self.list.remove("firstExample")
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.get(0), "secondExample")

    def test_remove_element_throws_exception_when_not_found(self):
        self.list.add("firstExample")
        with self.assertRaises(ValueError):
            self.list.remove("nonExisting")

    def test_get_element(self):
        self.list.add("firstExample")
        self.list.add("secondExample")
        self.assertEqual(self.list.get(0), "firstExample")
        self.assertEqual(self.list.get(1), "secondExample")

    def test_get_element_throws_exception_when_out_of_bounds(self):
        self.list.add("firstExample")
        with self.assertRaises(IndexError):
            self.list.get(1)

    def test_set_element(self):
        self.list.add("firstExample")
        self.list.set(0, "updatedExample")
        self.assertEqual(self.list.get(0), "updatedExample")

    def test_set_element_throws_exception_when_out_of_bounds(self):
        self.list.add("firstExample")
        with self.assertRaises(IndexError):
            self.list.set(1, "newExample")

    def test_contains(self):
        self.list.add("firstExample")
        self.assertTrue(self.list.contains("firstExample"))
        self.assertFalse(self.list.contains("nonExisting"))

    def test_clear(self):
        self.list.add("firstExample")
        self.list.add("secondExample")
        self.list.clear()
        self.assertEqual(len(self.list), 0)

    def test_remove_all(self):
        self.list.add("firstExample")
        self.list.add("secondExample")
        self.list.remove_all()
        self.assertEqual(len(self.list), 0)

    def test_increase_capacity_on_full(self):
        self.list.add("firstExample")
        self.list.add("secondExample")
        self.list.add("thirdExample")
        self.list.add("fourthExample")
        self.assertEqual(len(self.list), 4)

    def test_remove_at_index(self):
        self.list.add("firstExample")
        self.list.add("secondExample")
        self.list.add("thirdExample")
        self.list.remove_at_index(1)
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list.get(1), "thirdExample")

    def test_remove_at_index_throws_exception_when_out_of_bounds(self):
        self.list.add("firstExample")
        with self.assertRaises(IndexError):
            self.list.remove_at_index(1)

if __name__ == '__main__':
    unittest.main()
