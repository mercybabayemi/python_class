import unittest

import divisionandplacement


class TestDivisionAndPlacement(unittest.TestCase):
    def test_that_function_returns_correct_value_with_even_length(self):
        word = "helllo"
        second_word = "ce"
        actual = divisionandplacement.get_place(word, second_word)
        expected = "helcello"
        self.assertEqual(actual, expected)

    def test_that_function_throws_exception_with_invalid_input(self):
        self.assertRaises(TypeError, divisionandplacement.get_place(1, 2))

    def test_that_function_returns_correct_value_with_a_odd_length(self):
        word_1 = "joy"
        second_word_1 = "ce"
        actual = divisionandplacement.get_place(word_1, second_word_1)
        expected = "joyce"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
