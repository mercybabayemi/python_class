import unittest

from src.stack_method import StackMethod


class StackMethodTest(unittest.TestCase):
    def setUp(self):
        self.stack = StackMethod()

    def test_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_stack_push_new_element(self):
        self.stack.push("Item")
        self.stack.push("Item1")
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 2)

    def test_stack_pop_element(self):
        self.stack.push("Item")
        self.stack.push("Item1")
        self.stack.push("Item2")
        popped = self.stack.pop()
        self.assertEqual(popped, "Item2")
        self.assertEqual(self.stack.size(), 2)

    def test_stack_peek_element(self):
        self.stack.push("Item")
        self.stack.push("Item1")
        self.stack.push("Item2")
        peeked = self.stack.peek()
        self.assertEqual(peeked, "Item2")
        self.assertEqual(self.stack.size(), 3)

    def test_stack_search_element(self):
        self.stack.push("Item")
        self.stack.push("Item1")
        self.stack.push("Item2")
        self.stack.push("Item3")
        self.assertEqual(self.stack.search("Item2"), 2)
        self.assertEqual(self.stack.search("Item4"), -1)

if __name__ == '__main__':
    unittest.main()