from unittest import TestCase
import dictionarykeyvaluefromlist

class TestDictionaryFunction(TestCase):
	def test_that_function_exist(self):
		num = 4
		dictionarykeyvaluefromlist.get_dictionary_value_squared(num)
	def test_that_function_returns_correct_value(self):
		num = 9
		actual = dictionarykeyvaluefromlist.get_dictionary_value_squared(num)
		expected = {1:9,2:81}
		self.assertEqual(actual,expected)
