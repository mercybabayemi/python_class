from unittest import TestCase
import semicolonstore

class TestSemiColonStore(TestCase):
	def test_that_function_exists(self):
		semicolonstore.major_display()

	def test_that_cube_function_return_correct_value(self):
		actual = semicolonstore.major_display()
		expected = """
			SEMICOLON STORES
			MAIN BRANCH
			LOCATION: 312, HERBERT MACAULAY WAY, SABO, YABA, LAGOS STATE
			TEL : 03293828343
			"""
		self.assertEqual(actual, expected)
	