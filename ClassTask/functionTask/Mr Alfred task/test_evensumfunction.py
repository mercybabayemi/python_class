from unittest import TestCase
import evensumfunction

class TestEvenNumberSumFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [2,7,9,17,19,2,8,10]
		evensumfunction.is_even(numbers)
	
	def test_that_function_return_correct_value(self):
		numbers = [2,7,9,17,19,2,8,10,20]
		actual = evensumfunction.is_even(numbers)
		expected = 42
		self.assertEqual(actual, expected)