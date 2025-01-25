from unittest import TestCase
import numbersquarefunction

class TestOddSquareFunction(TestCase):
	def test_that_function_exist(self):
		user_input = 5
		numbersquarefunction.get_number_square(user_input)
	
	def test_that_function_return_correct_value(self):
		user_input = 5
		actual =numbersquarefunction.get_number_square(user_input)
		expected = [1,4,9,16]
		self.assertEqual(actual, expected)