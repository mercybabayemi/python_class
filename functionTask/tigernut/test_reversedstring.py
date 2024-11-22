from unittest import TestCase
import reversedstring

class TestReversedString(TestCase):
	def test_that_function_exist(self):
		word = "hello"
		reversedstring.get_reversed_string(word)
	def test_that_function_return_correct_value(self):
		word = "hello"
		actual = reversedstring.get_reversed_string(word)
		self.assertTrue(actual)
