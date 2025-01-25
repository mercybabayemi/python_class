from unittest import TestCase
import primenumberfunctiontask

class TestPrimeNumberFunctionTask(TestCase):
	def test_that_function_exist(self):
		number = 20
		primenumberfunctiontask.get_prime(number)
	
	def test_that_function_return_correct_value(self):
		number = 20
		actual = primenumberfunctiontask.get_prime(number)
		expected = [2,3,5,7,11,13,17,19]
		self.assertEqual(actual, expected)