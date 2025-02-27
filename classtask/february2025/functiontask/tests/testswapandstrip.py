import unittest

import swapandstrip


class TestCharacterFrequency(unittest.TestCase):
    def test_that_function_returns_correct_value(self):
        first_word = 'abc'
        second_word = 'xyz'
        actual = swapandstrip.swap_and_convert_characters(first_word, second_word)
        expected = "xyc abz"
        self.assertEqual(actual, expected)

    def test_that_function_throws_exception_with_invalid_input(self):
        self.assertRaises(TypeError, swapandstrip.swap_and_convert_characters, 1)


if __name__ == '__main__':
    unittest.main()