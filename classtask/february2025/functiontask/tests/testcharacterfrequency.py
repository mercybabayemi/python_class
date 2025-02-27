import unittest

from src.characterfrequency import get_character_frequency


class TestCharacterFrequency(unittest.TestCase):
    def test_that_function_returns_correct_value(self):
        word = 'semicolon.africa'
        actual = get_character_frequency(word)
        expected = {'s': 1, 'e': 1, 'm': 1, 'i': 2, 'c': 2, 'o': 2, 'l': 1, 'n': 1, '.': 1, 'a': 2, 'f': 1, 'r': 1}
        self.assertEqual(actual, expected)

    def test_that_function_throws_exception_with_invalid_input(self):
        self.assertRaises(TypeError, get_character_frequency(1))

    def test_that_function_returns_correct_value_with_a_character(self):
        character = 's'
        actual = get_character_frequency(character)
        expected = {'s': 1}
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
