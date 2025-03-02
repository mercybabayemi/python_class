import unittest

from src.sevensegment import SevenSegmentDisplay


class TestSevenSegmentDisplay(unittest.TestCase):
    def setUp(self):
        self.display = SevenSegmentDisplay()

    def test_user_inputs_non_binary_numbers(self):
        with self.assertRaises(ValueError):
            self.display.display_segment("1234s678")

    def test_user_inputs_more_than_8_digit_numbers(self):
        with self.assertRaises(ValueError):
            self.display.display_segment("010011101")

    def test_user_inputs_less_than_8_digit_numbers(self):
        with self.assertRaises(ValueError):
            self.display.display_segment("1110001")

    def test_given_11111100_board_is_off(self):
        self.display.display_segment("11111100")
        self.assertFalse(self.display.get_is_on())

    def test_given_11111101_board_is_on(self):
        self.display.display_segment("11111101")
        self.assertTrue(self.display.get_is_on())
        self.display.display_segment("11111100")
        self.assertFalse(self.display.get_is_on())

    def test_given_11111100_is_off_then_empty_string_is_displayed(self):
        self.assertFalse(self.display.get_is_on())
        expected_result = [[' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ']]
        self.assertEqual(expected_result, self.display.display_segment("11111100"))

    def test_given_11111101_board_is_on_when_displayed_then_hashtags_representing_0_is_displayed(self):
        actual = self.display.display_segment("11111101")
        self.assertTrue(self.display.get_is_on())
        expected = [['#', '#', '#', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', '#', '#', '#']]
        self.assertEqual(expected, actual)

    def test_given_01100001_board_is_on_when_displayed_then_hashtags_representing_1_is_displayed(self):
        actual = self.display.display_segment("01100001")
        self.assertTrue(self.display.get_is_on())
        expected = [[' ', ' ', ' ', ' '],
                    ['#', ' ', ' ', '#'],
                    ['#', ' ', ' ', '#'],
                    [' ', ' ', ' ', '#'],
                    [' ', ' ', ' ', ' ']]
        self.assertEqual(expected, actual)

    def test_given_11011011_board_is_on_when_displayed_then_hashtags_representing_2_is_displayed(self):
        actual = self.display.display_segment("11011011")
        self.assertTrue(self.display.get_is_on())
        expected = [['#', '#', '#', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', '#', '#', '#'],
                    [' ', ' ', ' ', ' '],
                    ['#', '#', '#', '#']]
        self.assertEqual(expected, actual)

    def test_given_11110011_board_is_on_when_displayed_then_hashtags_representing_3_is_displayed(self):
        actual = self.display.display_segment("11110011")
        self.assertTrue(self.display.get_is_on())
        expected = [['#', '#', '#', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', '#', '#', '#'],
                    [' ', ' ', ' ', '#'],
                    ['#', '#', '#', '#']]
        self.assertEqual(expected, actual)

    def test_given_01100111_board_is_on_when_displayed_then_hashtags_representing_4_is_displayed(self):
        actual = self.display.display_segment("01100111")
        self.assertTrue(self.display.get_is_on())
        expected = [[' ', ' ', ' ', ' '],
                    ['#', ' ', ' ', '#'],
                    ['#', '#', '#', '#'],
                    [' ', ' ', ' ', '#'],
                    [' ', ' ', ' ', ' ']]
        self.assertEqual(expected, actual)

    def test_given_10110111_board_is_on_when_displayed_then_hashtags_representing_5_is_displayed(self):
        actual = self.display.display_segment("10110111")
        self.assertTrue(self.display.get_is_on())
        expected = [['#', '#', '#', '#'],
                    [' ', ' ', ' ', ' '],
                    ['#', '#', '#', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', '#', '#', '#']]
        self.assertEqual(expected, actual)

    def test_given_10111111_board_is_on_when_displayed_then_hashtags_representing_6_is_displayed(self):
        actual = self.display.display_segment("10111111")
        self.assertTrue(self.display.get_is_on())
        expected = [['#', '#', '#', '#'],
                    ['#', ' ', ' ', ' '],
                    ['#', '#', '#', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', '#', '#', '#']]
        self.assertEqual(expected, actual)

    def test_given_11100001_board_is_on_when_displayed_then_hashtags_representing_7_is_displayed(self):
        actual = self.display.display_segment("11100001")
        self.assertTrue(self.display.get_is_on())
        expected = [['#', '#', '#', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', ' ', ' ', '#'],
                    [' ', ' ', ' ', '#'],
                    [' ', ' ', ' ', ' ']]
        self.assertEqual(expected, actual)

    def test_given_11111111_board_is_on_when_displayed_then_hashtags_representing_8_is_displayed(self):
        actual = self.display.display_segment("11111111")
        self.assertTrue(self.display.get_is_on())
        expected = [['#', '#', '#', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', '#', '#', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', '#', '#', '#']]
        self.assertEqual(expected, actual)

    def test_given_11110111_board_is_on_when_displayed_then_hashtags_representing_9_is_displayed(self):
        actual = self.display.display_segment("11110111")
        self.assertTrue(self.display.get_is_on())
        expected = [['#', '#', '#', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', '#', '#', '#'],
                    [' ', ' ', ' ', '#'],
                    ['#', '#', '#', '#']]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()