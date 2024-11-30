from unittest import TestCase
import doublednumber

class TestElementDoubledFunction(TestCase):
	def test_that_function_exist(self):
		element = [1,2,3,4,5]
		doublednumber.get_number_doubled(element)
	
	def test_that_function_return_correct_value(self):
		element = [1,2,3]
		actual = doublednumber.get_number_doubled(element)
		expected = [2,4,6]
		self.assertEqual(actual,expected)