"""write a function that takes in two numbers and multiply and return the result without using the * symbol. use TDD and ensure you write for possible edge cases
"""

from unittest import TestCase
import multiplicationpractie

class TestMultiplicationFunction(TestCase):
	def test_that_multiplication_function_exists(self):
		multiplicationpractice.get_multiply(3,3)
	
	def test_that_multiplication_function_return_correct_value(self):
		actual = multiplicationpractice.get_multiply(3,3)
		expected = 9
		self.assertEqual(actual,expected)
		


	