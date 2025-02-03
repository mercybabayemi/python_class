from unittest import TestCase
import sortlist

class TestSortingTwoList(TestCase):
	def test_that_function_exist(self):
		input_one =[3,4,9,10]
		input_two =[1,5,7,8]
		sortlist.get_merge(input_one, input_two)

	def test_that_function_return_correct_value(self):
		input_one = [3,4,9,10,-8]
		input_two = [1,5,7,8,72]
		actual = sortlist.get_merge(input_one, input_two)
		expected = [-8,1,3,4,5,7,8,9,10,72] 
		self.assertEqual(actual,expected)