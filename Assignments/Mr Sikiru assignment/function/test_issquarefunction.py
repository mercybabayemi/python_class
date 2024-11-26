from unittest import TestCase
import issquarefunction

class TestSquareFunction(TestCase):
	def test_that_function_exist(self):
		integer = 25
		issquarefunction.is_square(integer)
	
	def test_that_function_return_correct_value(self):
		integer = 25
		actual = issquarefunction.is_square(integer)
		expected = True
		self.assertEqual(actual, expected)
