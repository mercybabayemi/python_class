from unittest import TestCase
import evenfunction

class TestEvenNumberFunction(TestCase):
	def test_that_function_exist(self):
		integer = 8
		evenfunction.is_even(integer)
	
	def test_that_function_return_correct_value(self):
		integer = 8
		actual = evenfunction.is_even(integer)
		expected = True
		self.assertEqual(actual, expected)