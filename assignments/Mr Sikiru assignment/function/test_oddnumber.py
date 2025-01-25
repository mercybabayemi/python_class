from unittest import TestCase
import oddnumber

class TestNumberFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [57, 89, 64, 82, 45, 21]
		oddnumber.odd_position_numbers(numbers)
	
	def test_that_function_return_correct_value(self):
		numbers = [57, 89, 64, 82, 45, 21]
		actual = oddnumber.odd_position_numbers(numbers)
		expected = [57,89,45,21]
		self.assertEqual(actual, expected)