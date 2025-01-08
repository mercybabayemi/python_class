from unittest import TestCase
import wordswhitespaceremoval

class TestWhitespaceRemoval(TestCase):
	def test_that_function_exist(self):
		word = "hello world"
		wordswhitespaceremoval.get_whitespace_removal(word)
	def test_that_function_returns_correct_value(self):
		word = "hello world"
		actual = wordswhitespaceremoval.get_whitespace_removal(word)
		expected = "helloworld"
		self.assertEqual(actual,expected)