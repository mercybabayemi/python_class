from unittest import TestCase
import mergeandsortlist

class TestSortingTwoList(TestCase):
	def test_that_function_exist(self):
		input_one =[1,3,5]
		input_two =[2,4,6]
		mergeandsortlist.get_merged_and_sorted_list(input_one, input_two)

	def test_that_function_return_correct_value(self):
		input_one = [1,3,5]
		input_two = [2,4,6]
		actual = mergeandsortlist.get_merged_and_sorted_list(input_one, input_two)
		expected = [1,2,3,4,5,6] 
		self.assertEqual(actual,expected)