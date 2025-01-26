from unittest import TestCase
from class_task import numbers_between_20_to_50_list_comprehension

class TestListComprehensionFunction(TestCase):
    def test_that_function_exist(self):
        numbers = [12,15,19,21,50,70]
        numbers_between_20_to_50_list_comprehension.get_numbers(numbers)

        def test_that_function_return_correct_value(self):
            actual = numbers_between_20_to_50_list_comprehension.get_numbers(numbers)
            expected = [21,50]
            self.assertEqual(actual, expected)



