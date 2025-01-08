from unittest import TestCase
import stringacronym

class TestStringAcronym(TestCase):
	def test_that_function_exist(self):
		word = "Portable Graphic Network"
		stringacronym.get_string_acronym(word)

	def test_that_function_return_correct_value(self):
		word = "Portable Network Graphic"
		actual = stringacronym.get_string_acronym(word)
		expected = "PNG"
		self.assertEqual(actual,expected)