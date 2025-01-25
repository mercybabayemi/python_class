from unittest import TestCase
import multiplefunction

class TestEvenNumberSumFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
		multiplefunction.get_multiples(numbers)
	
	def test_that_function_return_correct_value(self):
		numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
		actual = multiplefunction.get_multiples(numbers)
		expected = [3,6,9,12,15,18,21,24,27,30]
		self.assertEqual(actual, expected)