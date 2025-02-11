from unittest import TestCase
import unzipvaluefromdictionary

class TestVowelRemovalFunction(TestCase):
	def test_that_function_exist(self):
		new_sample ={"names":"Alice", "age":25, "city":"New York"}
		unzipvaluefromdictionary.get_zip_value_as_list(new_sample)
	
	def test_that_function_return_correct_value(self):
		new_sample ={"names":"Alice", "age":25, "city":"New York"}
		actual = unzipvaluefromdictionary.get_zip_value_as_list(new_sample)
		expected = ["Alice", 25, "New York"]
		self.assertEqual(actual,expected) 