from unittest import TestCase
import stringanagramfunction

class TestAnagramStrings(TestCase):
	def test_that_function_exist(self):
		first_word = "listen"
		second_word = "silent"
		stringanagramfunction.get_string_anagram(first_word,second_word)
	def test_that_function_return_correct_value(self):
		first_word = "listen"
		second_word = "silent"
		actual = stringanagramfunction.get_string_anagram(first_word,second_word)
		expected = True
		self.assertEqual(actual, expected)