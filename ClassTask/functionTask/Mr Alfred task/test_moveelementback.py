from unittest import TestCase
import moveelementback

class TestElementFunction(TestCase):
	def test_that_function_exist(self):
		x = [1,2,3,4,5]
		y = 2
		moveelementback.get_element_movement(x,y)
	
	def test_that_function_return_correct_value(self):
		x = [1,2,3,4,5]
		y = 2
		actual = moveelementback.get_element_movement(x,y)
		expected = [3, 4, 5, 1, 2]
		self.assertEqual(actual,expected)