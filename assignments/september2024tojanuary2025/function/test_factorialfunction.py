from unittest import TestCase
import factorialfunction

class TestSquareFunction(TestCase):
	def test_that_function_exist(self):
		integer = 5
		factorialfunction.factorial_of(integer)
	
	def test_that_function_return_correct_value(self):
		integer = 5
		actual = factorialfunction.factorial_of(integer)
		expected = 120
		self.assertEqual(actual, expected)