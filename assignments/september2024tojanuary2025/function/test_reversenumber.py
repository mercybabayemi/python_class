from unittest import TestCase
import reversenumber

class TestNumberFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [57, 89, 64, 82, 45, 21]
		reversenumber.reversed_list(numbers)
	
	def test_that_function_return_correct_value(self):
		numbers = [57, 89, 64, 82, 45, 21]
		actual = reversenumber.reversed_list(numbers)
		expected = [21,45,82,64,89,57]
		self.assertEqual(actual, expected)