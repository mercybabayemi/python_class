from unittest import TestCase
import primefunction

class TestPrimeNumberFunction(TestCase):
	def test_that_function_exist(self):
		integer = 7
		primefunction.is_prime_number(integer)
	
	def test_that_function_return_correct_value(self):
		integer = 7
		actual = primefunction.is_prime_number(integer)
		expected = True
		self.assertEqual(actual, expected)