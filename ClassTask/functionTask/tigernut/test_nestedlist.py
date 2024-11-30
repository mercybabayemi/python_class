from unittest import TestCase
import nestedlist

class TestNesteListFunction(TestCase):
	def test_that_function_exist(self):
		x = [1,2,3,4,5]
		nestedlist.get_two_list(x)
	
	def test_that_function_return_correct_value(self):
		x = [1,2,3,4,5]
		actual = nestedlist.get_two_list(x)
		expected = [[1,2,3],[4,5]]
		nestedlist.get_two_list(x)