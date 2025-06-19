import unittest

from src import get_time

class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = get_time.time_in_words()
        actual = "one fifty PM"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
