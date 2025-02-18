import unittest
from string import ascii_letters

from generating_password import Generator

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()
    def test_that_password_is_an_empty_string(self):
        self.assertEqual("", self.generator.get_password())
    def test_that_password_contains_16_characters(self):
        self.generator.set_password()
        self.assertEqual(16, len(self.generator.get_password()))

if __name__ == '__main__':
    unittest.main()
