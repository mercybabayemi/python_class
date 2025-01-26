from unittest import TestCase
from class_task import populated_dictionary


class MyTestCase(TestCase):
    def test_that_function_exist(self):
        list1 = ["cohort24", "cohort23", "cohort22", "cohort21", "cohort20"]
        list2 = ["4 months", "5 months", "6 months", "7 months", "8 months"]
        populated_dictionary.get_populate_dictionary(list1, list2)

    def test_that_function_return_correct_value(self):
        list1 = ["cohort24", "cohort23", "cohort22", "cohort21", "cohort20"]
        list2 = ["4 months", "5 months", "6 months", "7 months", "8 months"]
        actual = populated_dictionary.get_populate_dictionary(list1, list2)
        expected = {"cohort24":"4 months", "cohort23":"5 months", "cohort22":"6 months", "cohort21":"7 months", "cohort20":"8 months"}
        self.assertEqual(actual, expected)
