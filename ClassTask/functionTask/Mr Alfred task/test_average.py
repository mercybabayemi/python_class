from unittest import TestCase
import average

class TestAverageFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [55,65,75,85]
		average.get_list_average(numbers)

	def test_that_function_return_correct_value(self):
		numbers = [55,65,75,85]
		actual = average.get_list_average(numbers)
		expected = 70
		self.assertEqual(actual,expected)
		numbers = [10,20,30,40]
		actual = average.get_list_average(numbers)
		expected = 25
		self.assertEqual(actual,expected)
	