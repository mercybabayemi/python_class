from unittest import TestCase
import elementdigitfunction

class TestOddSquareFunction(TestCase):
	def test_that_function_exist(self):
		elements = 'abc123def456'
		elementdigitfunction.get_digit_numbers(elements)
	
	def test_that_function_return_correct_value(self):
		elements = 'abc123def456'
		actual = elementdigitfunction.get_digit_numbers(elements)
		expected = [1,2,3,4,5,6]
		self.assertEqual(actual, expected)