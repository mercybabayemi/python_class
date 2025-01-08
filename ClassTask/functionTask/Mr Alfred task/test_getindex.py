from unittest import TestCase
import getindex

class TestIndexFunction(TestCase):
	def test_that_index_function_exists(self):
		input = [12,17,24,32,14]
		getindex.get_index(input, 24)

	def test_that_cube_function_return_correct_value(self):
		input = [12,17,24,32,14]
		actual = getindex.get_index(input, 24)
		expected = 2
		self.assertEqual(actual, expected)
		input = [12,17,24,32,14]
		actual = getindex.get_index(input, 54)
		expected = "not available"
		self.assertEqual(actual, expected)
	def test_that_get_index_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, getindex.get_index,"rrrr")