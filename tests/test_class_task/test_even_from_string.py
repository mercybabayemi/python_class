from unittest import TestCase
from class_task import even_from_string


class MyTestCase(TestCase):
    def test_that_function_exist(self):
        message = "73H2AdsdF439dm"
        even_from_string.get_even_from_string(message)

    def test_that_function_return_correct_value(self):
        message = "73H2AdsdF439dm"
        actual = even_from_string.get_even_from_string(message)
        expected = [2,4]
        self.assertEqual(actual, expected)


