from unittest import TestCase
import evensum

class TestSumFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [1,2,3,4,5]
		evensum.get_sum(numbers)
	def test_that_cube_function_return_correct_value(self):
		numbers = [1,2,3,4,5]
		actual = evensum.get_sum(numbers)
		expected = 6
		self.assertEqual(actual, expected)
		numbers = [1,2,3,4,5,6,7,8,9,10]
		actual = evensum.get_sum(numbers)
		expected = 30
		self.assertEqual(actual, expected)

