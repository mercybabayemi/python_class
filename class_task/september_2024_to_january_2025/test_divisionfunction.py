from unittest import TestCase
import divisionfunction

class TestSquarerootFunction(TestCase):
	def test_that_function_exist(self):
		divisionfunction.get_squareroot(10)

	def test_that_function_returns_correct_value(self):
		actual = divisionfunction.get_squareroot(10)
		expected = 3.16
		self.assertEqual(actual, expected)

	def test_that_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, divisionfunction.get_squareroot, "String")
		self.assertRaises(TypeError, divisionfunction.get_squareroot, " ")
	def test_that_function_returns_correct_value_with_float(self):
		actual =divisionfunction.get_squareroot(10.0)
		expected = 3.16
		self.assertEqual(actual, expected)
		