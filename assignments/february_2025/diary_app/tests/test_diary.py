import unittest
from diary import Diary, Entry

class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("username", "password")

    def test_that_diary_is_unlocked_when_password_is_correct(self):
        self.diary.unlock_diary("password")
        self.assertFalse(self.diary.is_locked)

    def test_that_diary_is_locked_when_password_is_incorrect_to_unlock_diary(self):
        self.diary.unlock_diary("wrongpass")
        self.assertTrue(self.diary.is_locked)

    def test_that_diary_is_locked_when_lock_diary_is_used(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked)

    def test_that_diary_create_entry_and_add_to_entries(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.assertEqual(self.diary.size(), 3)

    def test_that_diary_create_entry_and_delete_entry_remove_from_entries(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.assertEqual(self.diary.size(), 3)
        self.diary.delete_entry(2)
        self.assertEqual(self.diary.size(), 2)

    def test_that_diary_create_entry_and_delete_entry_throws_exception_when_id_is_negative_or_greater_than_entry_count(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        with self.assertRaises(IndexError):
            self.diary.delete_entry(-1)
        with self.assertRaises(IndexError):
            self.diary.delete_entry(4)

    def test_that_diary_find_entry_by_id_and_return_entry(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        entry_found = self.diary.find_entry_by_id(2)
        self.assertEqual(entry_found.get_id(), 2)

    def test_that_diary_find_entry_by_id_throws_exception_when_id_is_negative_or_greater_than_entry_count(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        with self.assertRaises(IndexError):
            self.diary.find_entry_by_id(-1)
        with self.assertRaises(IndexError):
            self.diary.find_entry_by_id(4)

    def test_that_diary_update_entry(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.update_entry(1, "newTitle", "newBody")
        self.assertEqual(self.diary.size(), 2)
        self.assertEqual(self.diary.find_entry_by_id(1).get_entry_body(), "newBody")
        self.assertEqual(self.diary.find_entry_by_id(1).get_title(), "newTitle")

    def test_that_diary_update_entry_throws_exception_when_id_is_negative_or_does_not_exist_or_greater_than_entry_count(self):
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        self.diary.create_entry("Title", "Entry Body")
        with self.assertRaises(IndexError):
            self.diary.update_entry(-1, "newTitle", "newBody")
        with self.assertRaises(IndexError):
            self.diary.update_entry(5, "newTitle", "newBody")

if __name__ == '__main__':
    unittest.main()