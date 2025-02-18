from unittest import TestCase
import stringpalindromefunction

class TestStringPalindrome(TestCase):
	def test_that_function_return_correct_value(self):
		word = "madam"
		stringpalindromefunction.get_string_palindrome(word)

	def test_that_function_returns_correct_value(self):
		actual = "madam"
		expected = "madam"
		self.assertEqual(actual,expected)