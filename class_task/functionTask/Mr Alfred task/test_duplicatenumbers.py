from unittest import TestCase
import duplicatenumbers

class TestDuplicateNumbers(TestCase):
	def test_that_function_exist(self):
		numbers = [1,2,3,4,5,2]
		duplicatenumbers.find_duplicate(numbers)
	def test_that_function_returns_correct_value(self):
		numbers = [1,2,3,4,5,2]
		actual = duplicatenumbers.find_duplicate(numbers)
		expected = True
		self.assertEqual(actual,expected)