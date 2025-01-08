from unittest import TestCase
import palindromelistfunction

class TestOddSquareFunction(TestCase):
	def test_that_function_exist(self):
		words = ['madam', 'apple', 'racecar']
		palindromelistfunction.get_is_palindrome(words)
	
	def test_that_function_return_correct_value(self):
		words = ['madam', 'apple', 'racecar']
		actual = palindromelistfunction.get_is_palindrome(words)
		expected = [True,False,True]
		self.assertEqual(actual, expected)