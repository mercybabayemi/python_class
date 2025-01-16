from unittest import TestCase
import evennumberfromstring

class TestEvenFunction(TestCase):
	def test_that_even_number_exists(self):
		message = "73H2AdsdF439dm"
		evennumberfromstring.get_even_number(message)
	def test_that_even_number_returns_correct_value(self):
		message = "73HAdsdF39dm"
		actual = evennumberfromstring.get_even_number(message)
		expected = []
		self.assertEqual(actual,expected)