from unittest import TestCase
import oddnumberssum

class TestDigitsOddNumberSum(TestCase):
	def test_that_function_exist(self):
		numbers = 12345
		oddnumberssum.get_sum_of_odd_digits(numbers)
	def test_that_function_returns_correct_value(self):
		numbers = 12345
		actual = oddnumberssum.get_sum_of_odd_digits(numbers)
		expected = 9
		self.assertEqual(actual,expected)