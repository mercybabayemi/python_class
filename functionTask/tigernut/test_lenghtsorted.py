from unittest import TestCase
import lenghtsorted

class TestSortByLength(TestCase):
	def test_that_function_exist(self):
		words = ["apple","cashew","cherry"]
		lenghtsorted.get_sorted_lenght(words)
	def test_that_function_returns_correct_value(self):
		words = ["apple","cashews","cherry"]
		actual = lenghtsorted.get_sorted_lenght(words)
		expected = ["apple","cherry","cashews"]
		self.assertEqual(actual,expected)