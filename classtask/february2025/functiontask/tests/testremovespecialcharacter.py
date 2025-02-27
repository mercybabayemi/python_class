import unittest

import removespecialcharacter


class TestRemoveSpecialCharacter(unittest.TestCase):
    def test_that_function_returns_correct_value(self):
        word = 'he,ll.o'
        actual = removespecialcharacter.remove_special_characters(word)
        expected = "hello"
        self.assertEqual(actual, expected)

    def test_that_function_throws_exception_with_invalid_input(self):
        self.assertRaises(TypeError, removespecialcharacter.remove_special_characters, 2)


if __name__ == '__main__':
    unittest.main()
