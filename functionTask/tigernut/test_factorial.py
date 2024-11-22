from unittest import TestCase
import factorial

class TestFactorialResult(TestCase):
	def test_that_function_exist(self):
		number = 5
		factorial.get_factorial(number)
	def test_that_function_returns_correct_value(self):
		number = 5
		actual = factorial.get_factorial(number)
		expected = 120
		self.assertEqual(actual,expected)