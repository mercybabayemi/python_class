from unittest import TestCase
import studentsubjectscores

class TestScoreFunction (TestCase):
	def test_that_function_exist(self):
		studentsubjectscores.get_score([],["python", "java", "data science", "critical thinking"]
, [])
	def test_that_function_return_correct_value(self):
		actual = studentsubjectscores.get_score(students, subjects, score)
		students = []
		scores = []
		subjects = ["python", "java", "data science", "critical thinking"]
		expected = studentsubjectscores.get_score([],  ["python", "java", "data science", "critical thinking"]
, [])
		self.assertEquals(actual,expected)
		