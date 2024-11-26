from unittest import TestCase
import square

class TestSquareFunction(TestCase):
	def test_that_function_exist(self):
		integer = 5
		square.square_of(integer)
	
	def test_that_function_return_correct_value(self):
		integer = 5
		actual = square.square_of(integer)
		expected = 25
		self.assertEqual(actual, expected)