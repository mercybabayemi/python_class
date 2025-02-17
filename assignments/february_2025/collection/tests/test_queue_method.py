import unittest

from src.queue_method import QueueMethod


class QueueMethodTest(unittest.TestCase):
    def setUp(self):
        self.queue = QueueMethod()

    def test_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_queue_add_when_not_full(self):
        self.queue.add("firstElement")
        self.assertFalse(self.queue.is_empty())
        self.queue.add("secondElement")
        self.queue.add("thirdElement")
        self.assertEqual(len(self.queue), 3)

    def test_queue_add_throws_exception(self):
        with self.assertRaises(ValueError):
            self.queue.add(None)
        self.queue.add("firstElement")
        self.queue.add("secondElement")
        self.queue.add("thirdElement")
        with self.assertRaises(OverflowError):
            self.queue.add("fourthElement")

    def test_queue_is_not_empty_after_offer(self):
        self.queue.offer("firstElement")
        self.assertFalse(self.queue.is_empty())

    def test_queue_is_full_and_cannot_add_element(self):
        self.queue.offer("firstElement")
        self.queue.offer("secondElement")
        self.queue.offer("thirdElement")
        self.assertEqual(len(self.queue), 3)
        self.assertFalse(self.queue.offer("fourthElement"))
        self.assertEqual(len(self.queue), 3)

    def test_queue_peek_retrieve_head_without_removing_it(self):
        self.queue.offer("firstElement")
        self.queue.offer("secondElement")
        self.assertEqual(self.queue.peek(), "firstElement")

    def test_queue_poll_retrieve_head_and_remove_it(self):
        self.queue.offer("firstElement")
        self.queue.offer("secondElement")
        self.assertEqual(self.queue.poll(), "firstElement")
        self.assertEqual(len(self.queue), 1)

    def test_queue_poll_returns_none_if_queue_is_empty(self):
        self.assertIsNone(self.queue.poll())

    def test_queue_remove_throws_exception_if_queue_is_empty(self):
        self.assertIsNone(self.queue.remove())

    def test_queue_remove_removes_head(self):
        self.queue.offer("firstElement")
        self.queue.offer("secondElement")
        self.queue.remove()
        self.assertEqual(self.queue.peek(), "secondElement")
        self.queue.offer("thirdElement")
        self.assertEqual(len(self.queue), 2)

    def test_queue_element_retrieves_head_without_removing_it(self):
        self.queue.offer("firstElement")
        self.queue.offer("secondElement")
        self.assertEqual(self.queue.peek(), "firstElement")
        self.assertEqual(len(self.queue), 2)

    def test_queue_element_throws_exception_if_queue_is_empty(self):
        self.assertIsNone(self.queue.element())

if __name__ == '__main__':
    unittest.main()