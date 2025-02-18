from unittest import TestCase
import indexsumsubtraction

class TestIndexSum(TestCase):
	def test_that_function_exist(self):
		numbers = [1,2,3,4,5]
		indexsumsubtraction.get_index_sum(numbers)
	def test_that_function_return_correct_value(self):
		numbers = [1,2,3,4,5]
		actual = indexsumsubtraction.get_index_sum(numbers)
		expected = 60 
		self.assertEqual(actual, expected)

		numbers = [1,2,3]
		actual = indexsumsubtraction.get_index_sum(numbers)
		expected = 12
		self.assertEqual(actual, expected)
