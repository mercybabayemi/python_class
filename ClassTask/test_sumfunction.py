from unittest import TestCase
import sumfunction

class TestSumFunction(TestCase):
	def test_that_function_exists(self):
		x = [1,2,3,4,5]
		sumfunction.get_sum(x)

	def test_that_function_returns_correct_value(self):
		x = [1,2,3,4,5]
		actual = sumfunction.get_sum(x)
		expected = 15
		self.assertEqual(actual,expected)
	def test_that_function_returns_correct_value_with_floats(self):
		x = [1.1,2.2,3.3,4.4,5.5]
		actual = sumfunction.get_sum(x)
		expected = 16.5
		self.assertEqual(actual,expected)
		x = [1.1,2.2,3.3,4.4,5]
		actual = sumfunction.get_sum(x)
		expected = 16
		self.assertEqual(actual,expected)

	def test_that_function_returns_correct_value_with_negative_values(self):
		x = [-1,-2,-3,-4,-5]
		actual = sumfunction.get_sum(x)
		expected = -15
		self.assertEqual(actual,expected)
	def test_that_function_returns_exception_error_with_invalid_input():
		self.assertRaises(TypeError, sumfunction.get_sum, "String")
		self.assertRaises(TypeError, sumfunction.get_sum, " ")

		
	