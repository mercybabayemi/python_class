from unittest import TestCase
import largestnumber

class TestNumberFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [57, 89, 64, 82, 45, 21]
		largestnumber.largest_element(numbers)
	
	def test_that_function_return_correct_value(self):
		numbers = [57, 89, 64, 82, 45, 21]
		actual = largestnumber.largest_element(numbers)
		expected = 89
		self.assertEqual(actual, expected)