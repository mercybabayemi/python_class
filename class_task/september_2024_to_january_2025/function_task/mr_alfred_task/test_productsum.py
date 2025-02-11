from unittest import TestCase
import productsum

class TestSumSquares(TestCase):
	def test_that_function_exist(self):
		numbers = [1,2,3,4]
		productsum.get_product_sum(numbers)
	def test_that_function_returns_correct_value(self):
		numbers = [1,2,3,4]
		actual = productsum.get_product_sum(numbers)
		expected = 30
		self.assertEqual(actual,expected)