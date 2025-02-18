import unittest
import multiplicationpractise

class TestMultiplicationFunction(unittest.TestCase):
	def test_that_multiplication_function_exists(self):
		multiplicationpractise.get_multiply(3,3)
	
	def test_that_multiplication_function_return_correct_value(self):
		actual = multiplicationpractise.get_multiply(3,3)
		expected = 9
		self.assertEqual(actual,expected)
		actual = multiplicationpractise.get_multiply(5,5)
		expected = 25
		self.assertEqual(actual,expected)

	def test_that_multiplication_function_return_correct_value_when_negative(self):
		actual = multiplicationpractise.get_multiply(5,-10)
		expected = 50
		self.assertEqual(actual,expected)
		actual = multiplicationpractise.get_multiply(-5,-10)
		expected = 50
		self.assertEqual(actual,expected)
		actual = multiplicationpractise.get_multiply(-5,10)
		expected = 50
		self.assertEqual(actual,expected)
		

	