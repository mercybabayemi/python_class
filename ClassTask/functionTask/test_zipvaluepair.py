from unittest import TestCase
import zipvaluepair

class TestVowelRemovalFunction(TestCase):
	def test_that_function_exist(self):
		keys = ["names","age","city"]
		values = ["Alice",25,"New York"]
		zipvaluepair.zip_function_sample(keys,values)
	
	def test_that_function_return_correct_value(self):
		keys = ["names","age","city"]
		values = ["Alice",25,"New York"]
		actual = zipvaluepair.zip_function_sample(keys,values)
		expected = {"names":"Alice", "age":25, "city":"New York"}
		self.assertEqual(actual,expected) 