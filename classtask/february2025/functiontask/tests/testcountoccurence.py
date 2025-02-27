import unittest

from countoccurence import get_count_occurrence


class TestCountOccurrence(unittest.TestCase):
    def test_that_function_returns_correct_value(self):
        word = "semicolon"
        second_word = "o"

        actual = get_count_occurrence(word, second_word)
        expected = ('o',2)
        self.assertEqual(actual, expected)

    def test_that_function_throws_exception_with_invalid_input(self):
        self.assertRaises(TypeError,  get_count_occurrence(1,2))


if __name__ == '__main__':
    unittest.main()

