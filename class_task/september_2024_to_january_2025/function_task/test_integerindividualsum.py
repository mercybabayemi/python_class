from unittest import TestCase
import integerindividualsum

class TestNumberSumFunction(TestCase):
	def test_that_function_exist(self):
		numbers = 192374
		integerindividualsum.get_number_sum(numbers)
	
	def test_that_function_return_correct_value(self):
		numbers = 192374
		actual = integerindividualsum.get_number_sum(numbers)
		expected = 26
		self.assertEqual(actual,expected)