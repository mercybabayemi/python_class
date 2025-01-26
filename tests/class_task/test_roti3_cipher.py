from unittest import TestCase
from class_task import roti3_cipher


class TestRoti3Cipher(TestCase):
    def test_that_roti3_cipher_function_exist(self):
        roti3_cipher.encrypt_text("welcome,123")
    def test_that_roti3_cipher_function_returns_correct_value(self):
        actual = (roti3_cipher.encrypt_text("welcome,123"))
        expected = "jrypbzr,123"
        self.assertEqual(actual, expected)
