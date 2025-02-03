from unittest import TestCase
import diary_function


class TestDiaryFunctionRefactor(TestCase):
	def test_that_function_exists(self):
		diary_id = 1
		diary_date = "23-11-2024"
		diary_content = "This is my first diary"
		diary_function.add_diary(diary_id, diary_date, diary_content)

	def test_add_diary(self):
		actual = diary_function.add_diary(1, "23-11-2024", "This is my first diary")
		expected = "Diary entry created successfully!"
		self.assertEqual(actual,expected)

	def test_add_diary_function_added(self):
		actual = len(diary_function.diaries)
		self.assertEqual(actual,1)

	def test_update_diary(self):
		diary_function.add_diary(1, "21-12-2024", "Test diary content.")
		actual = diary_function.update_diary(1, new_content = "Updated diary content.")
		self.assertEqual(actual, "Diary entry updated successfully!")

	def test_update_diary_not_found(self):
		actual = diary_function.update_diary(999, new_content = "Non-existing diary content.")
		self.assertEqual(actual, "Diary entry not found!")

	def test_delete_diary(self):
		diary_function.add_diary(1, "21-12-2024", "Test diary content.")
		actual = diary_function.delete_diary(1)
		self.assertEqual(actual, "Diary entry removed successfully.")

	def test_delete_diary_not_found(self):
		actual = diary_function.delete_diary(999)
		self.assertEqual(actual, "Diary entry not found!")

	def test_view_diaries_is_empty(self):
		diary_function.diaries.clear()
		actual = diary_function.view_diaries()
		self.assertEqual(actual, "No diary entries found.")

	def test_view_diaries(self):
		diary_function.add_diary(1, "21-12-2024", "Test diary content.")
		actual = diary_function.view_diaries()
		self.assertIn("Diary ID: 1", actual)
		self.assertIn("Date: 21-12-2024", actual)
		self.assertIn("Content: Updated diary content.", actual)
		self.assertIn("Locked: False", actual)

