from unittest import TestCase
import stringpalindrome

class TestNumberFunction(TestCase):
	def test_that_function_exist(self):
		input = "madam"
		stringpalindrome.is_palindrome(input)
	
	def test_that_function_return_correct_value(self):
		input = "madam"
		actual = stringpalindrome.is_palindrome(input)
		expected = True
		self.assertEqual(actual, expected)