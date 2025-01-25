from unittest import TestCase
from class_task import dictionary_key_value_from_list

class TestDictionaryFunction(TestCase):
	def test_that_function_exist(self):
		num = 4
		dictionary_key_value_from_list.get_dictionary_value_squared(num)
	def test_that_function_returns_correct_value(self):
		num = 9
		actual = dictionary_key_value_from_list.get_dictionary_value_squared(num)
		expected = {1:9,2:81}
		self.assertEqual(actual,expected)
