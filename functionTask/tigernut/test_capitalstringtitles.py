from unittest import TestCase
import capitalstringtitles

class TestCapitalTitle(TestCase):
	def test_that_function_exist(self):
		words = ["apple", "banana", "cherry"]
		capitalstringtitles.get_new_capitalized_title(words)

	def test_that_function_returns_correct_value(self):
		words = ["apple", "banana", "cherry"]
		actual = capitalstringtitles.get_new_capitalized_title(words)
		expected =  ["Apple", "Banana", "Cherry"]
		self.assertEqual(actual,expected)