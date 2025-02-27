import unittest

from mixedcaseword import get_sorted_mixed_case_words

class TestCharacterFrequency(unittest.TestCase):
    def test_that_function_returns_correct_value(self):
        word = 'sEmIColOn'
        actual = get_sorted_mixed_case_words(word)
        expected = "EICOsmoln"
        self.assertEqual(actual, expected)

    def test_that_function_throws_exception_with_invalid_input(self):
        self.assertRaises(TypeError, get_sorted_mixed_case_words, 1)

    def test_that_function_returns_correct_value_with_number(self):
        word = 'sEmIC1o2lOn'
        actual = get_sorted_mixed_case_words(word)
        expected = "EICOsmoln12"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()