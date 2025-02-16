import unittest

from src.array import ArrayMethod


class TestArrayMethod(unittest.TestCase):
    def setUp(self):
        self.array = ArrayMethod()

    def test_array_is_empty(self):
        self.assertTrue(self.array.is_empty())

    def test_add_to_array(self):
        self.assertTrue(self.array.is_empty())
        self.array.add("first_example")
        self.assertEqual(self.array.get(0), "first_example")

    def test_is_not_empty_after_add(self):
        self.array.add("first_example")
        self.assertFalse(self.array.is_empty())

    def test_add_null(self):
        with self.assertRaises(ValueError):
            self.array.add(None)

    def test_add_at_index(self):
        self.array.add("first_example")
        self.array.add("second_example")
        self.array.add_at_index(1, "replacement_example")
        self.assertEqual(self.array.get(1), "replacement_example")

    def test_add_at_index_out_of_bound(self):
        self.array.add("first_example")
        self.array.add("second_example")
        with self.assertRaises(IndexError):
            self.array.add_at_index(2, "replacement_example")

    def test_is_full(self):
        self.array.add("first_example")
        self.array.add("second_example")
        self.array.add("third_example")
        self.assertTrue(self.array.is_full())
        with self.assertRaises(Exception):
            self.array.add("fourth_example")

    def test_get(self):
        self.array.add("first_example")
        self.array.add("second_example")
        self.assertEqual(self.array.get(0), "first_example")
        self.assertEqual(self.array.get(1), "second_example")

    def test_get_out_of_bound(self):
        self.array.add("firstExample")
        with self.assertRaises(IndexError):
            self.array.get(1)

    def test_set(self):
        self.array.add("firstExample")
        self.array.add("secondExample")
        self.array.set(1, "setExample")
        self.assertEqual(self.array.get(1), "setExample")

    def test_set_out_of_bound(self):
        self.array.add("firstExample")
        with self.assertRaises(IndexError):
            self.array.set(1, "setExample")

    def test_contains(self):
        self.array.add("firstExample")
        self.array.add("secondExample")
        self.assertTrue(self.array.contains("secondExample"))
        self.assertFalse(self.array.contains("thirdExample"))

    def test_remove(self):
        self.array.add("firstExample")
        self.array.add("secondExample")
        self.array.remove("firstExample")
        self.assertEqual(self.array.get(0), "secondExample")

    def test_remove_not_found(self):
        self.array.add("firstExample")
        with self.assertRaises(Exception):
            self.array.remove("thirdExample")

    def test_clear(self):
        self.array.add("firstExample")
        self.array.add("secondExample")
        self.array.clear()
        self.assertEqual(len(self.array), 0)

    def test_remove_at_index(self):
        self.array.add("firstExample")
        self.array.add("secondExample")
        self.array.remove_at_index(1)
        self.assertEqual(len(self.array), 1)
        self.assertEqual(self.array.get(0), "firstExample")

    def test_remove_at_index_out_of_bound(self):
        self.array.add("firstExample")
        with self.assertRaises(IndexError):
            self.array.remove_at_index(1)

if __name__ == '__main__':
    unittest.main()
