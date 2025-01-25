from unittest import TestCase
import ispalindromefunction

class TestSquareFunction(TestCase):
	def test_that_function_exist(self):
		integer = 121
		ispalindromefunction.is_palindrome(integer)
	
	def test_that_function_return_correct_value(self):
		integer = 121
		actual = ispalindromefunction.is_palindrome(integer)
		expected = True
		self.assertEqual(actual, expected)
