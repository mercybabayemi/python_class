from unittest import TestCase
import removefunction

class TestClassTestRemove(TestCase):
	def test_that_function_exist(self):
		number = [1,9,7,2,5,4]
		removefunction.get_remove(number)
	def test_that_function_return_correct_value(self):
		number = [1,9,7,2,5,4]
		actual= removefunction.get_remove([1,9,7,2,5,4])
		expected= [1,9,7,2,5]
		self.assertEqual(actual,expected)
