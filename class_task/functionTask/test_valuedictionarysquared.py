from unittest import TestCase
import valuedictionarysquared

class TestVowelRemovalFunction(TestCase):
	def test_that_function_exist(self):
		valuedictionarysquared.my_dict_even()
	
	def test_that_function_return_correct_value(self):
		actual = valuedictionarysquared.my_dict_even()
		expected = {2:4,4:16,6:36,8:64,10:100}
		self.assertEqual(actual,expected) 