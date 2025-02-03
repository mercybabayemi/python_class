from unittest import TestCase
import subtractionfunction

class TestSubtractFunction(TestCase):
	def test_that_function_exist(self):
		integer1 = 30
		integer2 = 10
		subtractionfunction.subtract(integer1,integer2)
	
	def test_that_function_return_correct_value(self):
		integer1 = 30
		integer2 = 10
		actual = subtractionfunction.subtract(integer1,integer2)
		expected = 20
		self.assertEqual(actual, expected)