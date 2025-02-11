from unittest import TestCase
import positiveandnegativecount

class TestIndexFunction(TestCase):
	def test_that_index_function_exists(self):
		input = [15,34,-1,24,-7,9]
		positiveandnegativecount.get_index_positive_count(input)

	def test_that_cube_function_return_correct_value(self):
		input = [15,34,-1,24,-7,9]
		actual = positiveandnegativecount.get_index_positive_count(input)
		expected = 4
		self.assertEqual(actual, expected)
		input =[15,34,-1,24,-7,9]
		actual = positiveandnegativecount.get_index_negative_count(input)
		expected = 2
		self.assertEqual(actual, expected)
	def test_that_positive_and_negative_count_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, positiveandnegativecount.get_index_negative_count,"rrrr")