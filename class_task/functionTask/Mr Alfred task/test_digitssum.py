from unittest import TestCase
import digitssum

class TestDigitsSum(TestCase):
	def test_that_function_exist(self):
		numbers = 15324
		digitssum.get_sum_of_digits(numbers)
	def test_that_function_returns_correct_value(self):
		numbers = 15324
		actual = digitssum.get_sum_of_digits(numbers)
		expected = 15
		self.assertEqual(actual,expected)