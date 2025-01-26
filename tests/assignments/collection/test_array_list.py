import unittest
from assignments.collection.array_list import ArrayList


class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.array = ArrayList()

    def test_is_empty(self):
        self.assertTrue(self.array.is_empty())

    def test_add(self):
        self.array.add(1)
        self.assertEqual(self.array.size(), 1)
        self.assertEqual(self.array.get(0), 1)

    def test_add_item_increases_size(self):
        self.array.add("item1")
        self.array.add("item2")
        self.assertEqual(self.array.size(), 2)

    def test_add_at_index(self):
        self.array.add("item1")
        self.array.add("item2")
        self.array.add_at(1, "item1.5")
        self.assertEqual(self.array.get(1), "item1.5")
        self.assertEqual(self.array.get(2), "item2")
        self.assertEqual(self.array.size(), 3)

    def test_index_out_of_bounds_on_get(self):
        self.array.add("item1")
        with self.assertRaises(IndexError):
            self.array.get(1)

    def test_index_out_of_bounds_on_set(self):
        self.array.add("item1")
        with self.assertRaises(IndexError):
            self.array.set(1, "item2")

    def test_remove_item(self):
        self.array.add("item1")
        self.array.add("item2")
        self.array.remove("item1")
        self.assertEqual(self.array.size(), 1)
        self.assertEqual(self.array.get(0), "item2")

    def test_remove_non_existent_item(self):
        self.array.add("item1")
        with self.assertRaises(ValueError):
            self.array.remove("item2")

    def test_clear(self):
        self.array.add("item1")
        self.array.add("item2")
        self.array.clear()
        self.assertEqual(self.array.size(), 0)
        self.assertTrue(self.array.is_empty())

    def test_contains(self):
        self.array.add("item1")
        self.array.add("item2")
        self.assertTrue(self.array.contains("item1"))
        self.assertFalse(self.array.contains("item3"))

    def test_increase_capacity(self):
        self.array.add("item1")
        self.array.add("item2")
        self.array.add("item3")
        self.array.add("item4")  # This should trigger a capacity increase
        self.assertEqual(self.array.size(), 4)
        self.assertEqual(self.array.get(3), "item4")


if __name__ == '__main__':
    unittest.main()
