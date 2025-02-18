from unittest import TestCase
import popfunction

class TestClassTestPop(TestCase):
	def test_that_function_exist(self):
		number = [1,9,7,2,5,4]
		popfunction.get_pop(number)
	def test_thet_second_function_return_correct_value(self):
		number = [1,9,7,2,5,4]
		actual= popfunction.get_pop([1,9,7,2,5,4])
		expected= [1,9,7,5,4]
		self.assertEqual(actual,expected)