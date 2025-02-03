from unittest import TestCase
import valuefetch

class TestGettingValue(TestCase):
	def test_that_function_exist(self):
		integers = [1,4,3,2,5,9]
		valuefetch.get_value(integers)

	def test_that_function_returns_correct_value(self):
		integers = [1,4,3,2,5,9]
		actual = valuefetch.get_value(integers)
		expected = [False,True,False,True,False,False]
		self.assertEqual(actual,expected)