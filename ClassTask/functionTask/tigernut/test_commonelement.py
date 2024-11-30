from unittest import TestCase
import commonelement

class TestElements(TestCase):
	def test_that_function_exist(self):
		list_one = [1,2,3]
		list_two = [3,4,5]
		commonelement.get_common_elements(list_one,list_two)
	def test_that_function_returns_correct_value(self):
		list_one = [1,2,3]
		list_two = [3,4,5]
		actual = commonelement.get_common_elements(list_one,list_two)
		expected = 3
		self.assertEqual(actual,expected)