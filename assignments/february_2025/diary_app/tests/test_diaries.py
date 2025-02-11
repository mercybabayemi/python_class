import unittest

from diaries import Diaries
from diary import Diary
from no_such_element_exception import NoSuchElementException


class TestDiaries(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("username", "password")
        self.diaries = Diaries()

    def test_diaries_add(self):
        self.diaries.add("username", "password")
        found = self.diaries.find_by_username("username")
        self.assertEqual("username", found.get_username())

    def test_diaries_find_by_username(self):
        self.diaries.add("username", "password")
        found = self.diaries.find_by_username("username")
        self.assertEqual("username", found.get_username())

    def test_diaries_find_by_username_throws_exception_when_not_found(self):
        self.diaries.add("username", "password")
        with self.assertRaises(NoSuchElementException):
            self.diaries.find_by_username("user")

    def test_diaries_delete_diary(self):
        self.diaries.add("username", "password")
        self.diaries.delete("username", "password")
        self.assertEqual(0, self.diaries.size())

    def test_diaries_delete_diary_throws_exception_when_not_found(self):
        with self.assertRaises(NoSuchElementException):
            self.diaries.delete("username", "password")

if __name__ == "__main__":
    unittest.main()