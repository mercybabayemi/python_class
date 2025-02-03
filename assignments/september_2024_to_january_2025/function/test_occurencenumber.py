from unittest import TestCase
import occurencenumber

class TestNumberFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [57, 89, 64, 82, 45, 21]
		element = 64
		occurencenumber.elementOccurance(numbers,element)
	
	def test_that_function_return_correct_value(self):
		numbers = [57, 89, 64, 82, 45, 21]
		element = 64
		actual = occurencenumber.elementOccurance(numbers,element)
		expected = "Element exist in list at index"
		self.assertEqual(actual, expected)