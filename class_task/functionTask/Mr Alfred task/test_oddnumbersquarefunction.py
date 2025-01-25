from unittest import TestCase
import oddnumbersquarefunction

class TestOddSquareFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [10,3,7,1,9,4,2,8,5,6]zzzz
		oddnumbersquarefunction.get_odd_square(numbers)
	
	def test_that_function_return_correct_value(self):
		numbers = [10,3,7,1,9,4,2,8,5,6]
		actual = oddnumbersquarefunction.get_odd_square(numbers)
		expected = [9,49,1,81,25]
		self.assertEqual(actual, expected)