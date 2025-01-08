from unittest import TestCase
import greaternumberfunction

class TestOddSquareFunction(TestCase):
	def test_that_function_exist(self):
		number = [1,5,12,15,8]
		greaternumberfunction.get_number_greater_than_ten(number)
	
	def test_that_function_return_correct_value(self):
		number = [1,5,12,15,8]
		actual = greaternumberfunction.get_number_greater_than_ten(number)
		expected = [12,15]
		self.assertEqual(actual, expected)