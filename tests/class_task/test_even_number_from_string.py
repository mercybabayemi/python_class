from unittest import TestCase
from class_task import even_number_from_string

class TestEvenFunction(TestCase):
	def test_that_even_number_exists(self):
		message = "73H2AdsdF439dm"
		even_number_from_string.get_even_number(message)
	def test_that_even_number_returns_correct_value(self):
		message = "73HAdsdF39dm"
		actual = even_number_from_string.get_even_number(message)
		expected = []
		self.assertEqual(actual,expected)
