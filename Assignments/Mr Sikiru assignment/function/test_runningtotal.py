from unittest import TestCase
import runningtotal

class TestNumberFunction(TestCase):
	def test_that_function_exist(self):
		numbers = [57, 89, 64, 82, 45, 21]
		runningtotal.running_total_computed(numbers)
	
	def test_that_function_return_correct_value(self):
		numbers = [57, 89, 64, 82, 45, 21]
		actual = runningtotal.running_total_computed(numbers)
		expected = 358
		self.assertEqual(actual, expected)