import unittest

from diary import Diary
from security_error import SecurityError


class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("username,", "password")

    def test_diary_is_unlocked_when_password_is_correct(self):
        self.diary.unlock_diary("password")
        self.assertFalse(self.diary.is_locked)

    def test_diary_is_locked_when_password_is_incorrect(self):
        with self.assertRaises(SecurityError):
            self.diary.unlock_diary("pass")

    def test_diary_is_locked_when_lock_diary_is_used(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked)

    def test_diary_create_entry_and_add_to_entries(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.assertEqual(3, self.diary.size())

    def test_diary_create_entry_and_delete_entry_remove_from_entries(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.assertEqual(3, self.diary.size())
        self.diary.delete_entry(2)
        self.assertEqual(2, self.diary.size())

    def test_diary_create_entry_and_delete_entry_throws_exception_when_id_is_negative_or_greater_than_entry_count(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        with self.assertRaises(IndexError):
            self.diary.delete_entry(-1)
        with self.assertRaises(IndexError):
            self.diary.delete_entry(4)

    def test_diary_find_entry_by_id_and_return_entry(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        entry_found = self.diary.find_entry_by_id(2)
        self.assertEqual(2, entry_found.get_id())

    def test_diary_find_entry_by_id_throws_exception_when_id_is_negative_or_greater_than_entry_count(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        with self.assertRaises(IndexError):
            self.diary.find_entry_by_id(-1)
        with self.assertRaises(IndexError):
            self.diary.find_entry_by_id(4)

    def test_diary_update_entry(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.update_entry(1, "New Title", "New Body")
        self.assertEqual(2, self.diary.size())
        self.assertEqual("New Body", self.diary.find_entry_by_id(1).get_entry_body())
        self.assertEqual("New Title", self.diary.find_entry_by_id(1).get_title())

    def test_diary_update_entry_throws_exception_when_id_is_negative_or_does_not_exist_or_greater_than_entry_count(
            self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        with self.assertRaises(IndexError):
            self.diary.update_entry(-1, "newTitle", "newBody")
        with self.assertRaises(IndexError):
            self.diary.update_entry(5, "newTitle", "newBody")

if __name__ == "__main__":
    unittest.main()