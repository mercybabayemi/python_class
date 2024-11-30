from unittest import TestCase
import characterelementcount

class TestElementDoubledFunction(TestCase):
	def test_that_function_exist(self):
		words = ["apple", "fish", "orange", "ice", "lime"]
		characterelementcount.get_character_count(words)
	
	def test_that_function_return_correct_value(self):
		words = ["apple", "fish", "orange", "ice", "lime"]
		actual = characterelementcount.get_character_count(words)
		expected = ["apple","orange"]
		self.assertEqual(actual,expected)