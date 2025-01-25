from unittest import TestCase
import primenumberfunction

class TestPrimeNumbers(TestCase):
	def test_that_function_exist(self):
		numbers = 29
		primenumberfunction.get_prime_number(numbers)
	def test_that_function_return_correct_value(self):
		numbers = 29
		actual = primenumberfunction.get_prime_number(numbers)
		expected = True
		self.assertEqual(actual,expected)
		numbers = 2
		actual = primenumberfunction.get_prime_number(numbers)
		expected = True
		self.assertEqual(actual,expected)