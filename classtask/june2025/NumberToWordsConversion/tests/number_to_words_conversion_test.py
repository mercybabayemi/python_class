import unittest

from number_to_words_conversion import Conversion


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.conversion_source = Conversion()

    def test_that_number_1_to_10_returns_correct_value(self):
        actual = "One"
        expected = self.conversion_source.convert("1")
        self.assertEqual(expected, actual)
        actual_1 = "Ten"
        expected_1 = self.conversion_source.convert("10")
        self.assertEqual(expected_1, actual_1)

    def test_that_number_10_to_20_returns_correct_value(self):
        actual = "Twenty"
        expected = self.conversion_source.convert("20")
        self.assertEqual(expected, actual)
        actual_2 = "Fifteen"
        expected_2 = self.conversion_source.convert("15")
        self.assertEqual(expected_2, actual_2)

    def test_that_number_20_to_99_returns_correct_value(self):
        actual = "Ninety Seven"
        expected = self.conversion_source.convert("97")
        self.assertEqual(expected, actual)
        actual_3 = "Twenty Nine"
        expected_3 = self.conversion_source.convert("29")
        self.assertEqual(expected_3, actual_3)

    def test_that_number_100_to_999_returns_correct_value(self):
        actual = "Five Hundred and Fifty Three"
        expected = self.conversion_source.convert("553")
        self.assertEqual(expected, actual)
        actual_3 = "Nine Hundred and Ninety Seven"
        expected_3 = self.conversion_source.convert("997")
        self.assertEqual(expected_3, actual_3)



if __name__ == '__main__':
    unittest.main()
