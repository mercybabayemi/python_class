import unittest

from src.linked_list import LinkedListMethod

class LinkedListMethodTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedListMethod()

    def test_linked_list_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())

    def test_linked_list_add_elements(self):
        self.linked_list.add("first")
        self.linked_list.add("second")
        self.linked_list.add("third")
        self.assertFalse(self.linked_list.is_empty())
        self.assertEqual(len(self.linked_list), 3)

    def test_linked_list_remove_elements(self):
        self.linked_list.add("first")
        self.linked_list.add("second")
        self.linked_list.add("third")
        self.linked_list.remove("second")
        self.assertEqual(len(self.linked_list), 2)
        self.linked_list.remove("first")
        self.assertEqual(len(self.linked_list), 1)
        self.linked_list.remove("third")
        self.assertTrue(self.linked_list.is_empty())

if __name__ == '__main__':
    unittest.main()
