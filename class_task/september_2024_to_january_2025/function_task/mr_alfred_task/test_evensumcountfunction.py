from unittest import TestCase
import evensumcountfunction

class TestEvenNumberSumFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [1,5,7,3,2,9,8,10,]
		evensumcountfunction.get_even_count(numbers)
	
	def test_that_function_return_correct_value(self):
		numbers = [1,5,7,3,2,9,8,10,]
		actual = evensumcountfunction.get_even_count(numbers)
		expected = 3
		self.assertEqual(actual, expected)