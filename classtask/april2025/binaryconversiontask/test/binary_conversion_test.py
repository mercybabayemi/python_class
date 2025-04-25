import unittest

import binary_conversion


class MyTestCase(unittest.TestCase):

    def test_that_function_exist(self):
        number = "10"
        binary_conversion.convert_binary_to_base_ten(number)

    def test_that_function_returns_correct_value(self):
        self.assertEqual(2, binary_conversion.convert_binary_to_base_ten("10"))
        self.assertEqual(3, binary_conversion.convert_binary_to_base_ten("11"))

if __name__ == '__main__':
    unittest.main()
