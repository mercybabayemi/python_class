from unittest import TestCase
import divisionfunction

class TestDivideFunction(TestCase):
	def test_that_function_exist(self):
		integer1 = 30
		integer2 = 10
		divisionfunction.divide(integer1, integer2)
	
	def test_that_function_return_correct_value(self):
		integer1 = 30
		integer2 = 10
		actual = divisionfunction.divide(integer1, integer2)
		expected = 3.0
		self.assertEqual(actual, expected)
