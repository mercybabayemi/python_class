from unittest import TestCase
import vowelcount

class TestVowelFunction(TestCase):
	def test_that_function_exist(self):
		words = "python is sweet"
		vowelcount.get_vowel_count(words)
	def test_that_function_return_correct_value(self):
		words = "python is sweet"
		actual = vowelcount.get_vowel_count(words)
		expected = 4
		self.assertEqual(actual,expected)
		words = "I am beautiful"
		actual = vowelcount.get_vowel_count(words)
		expected = 7
		self.assertEqual(actual,expected)