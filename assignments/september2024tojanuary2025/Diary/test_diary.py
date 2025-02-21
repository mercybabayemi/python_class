from unittest import TestCase
import diary

class TestDiaryFunction(TestCase):
	def test_that_function_exists(self):
		diary_id = 1
		diary_date = "23-11-2024"
		diary_content = "This is my first diary"
		diary.add_diary(diary_id, diary_date, diary_content)

	