import sys
def get_student_number(title, teacher):
	number_of_students = int(input(f"{title} {teacher}, how many students do you have? \n"))

	print("Saving>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nSaved successfully.\n")
	return number_of_students

def get_subjects(title, teacher):
	student_subjects = int(input(f"{title} {teacher} how many subjects do you want to grade the students on? \n"))
	print("Saving>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nSaved successfully.\n")
	return student_subjects

def get_score(students, subjects, student_grade):
	for row in range(students):
		for column in range(subjects):
			student_grade[row][column] = int(input(f"Enter a number between 1 - 100 as score for student {row + 1}, Subject{column + 1}: "))
			while(student_grade[row][column] < 0 or student_grade[row][column] > 100):
				student_grade[row][column] = int(input("Invalid input!!!\nEnter a valid input: "))
			print("Saving>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nSaved successfully.")

def display_table_header(subjects):
	print("==========================================================================================\n")
	print(f"STUDENT\t {"\t".join([f"SUB {i + 1}" for i in range(subjects)])} \tTOT \tAVE \tPOS")
	print("\n==========================================================================================\n")

def display_table_content(student_grade, subjects, students):
	average_scores = [0] * students
	for row in range(students):
		subject_total = 0
		for column in range(subjects):
			subject_total += student_grade[row][column]
		average_scores[row] = float(subject_total / subjects)

	for row in range(students):
		print(f"Student ({row + 1})", end = "\t")
		subject_total = 0
		for column in range(subjects):
			print(f"{student_grade[row][column]}", end = "\t")
			subject_total += student_grade[row][column]
			
		print(f"{subject_total}\t{average_scores[row]}", end = "\t")
		average_score = average_scores[row]
		position = 1
		for i in range(students):
			if average_scores[i] > average_score:
				position += 1
		print(position)
		print("\n")
	print("\n==========================================================================================\n")

def get_subject_calculated(student_grade, subjects, students):
	pass_mark = 50
	for column in range(subjects):
		highest_score = -1
		highest_index = ""
		lowest_score = sys.maxsize
		lowest_index = ""
		subject_total = 0
		average_subject_score = 0
		pass_count = 0
		fail_count = 0
		print(f"Subject {column + 1} \t")
		for row in range(students):
			subject_total += student_grade[row][column]
			if student_grade[row][column] >= highest_score:
				highest_score = student_grade[row][column]
				highest_index = f"Student {row + 1}"
			if student_grade[row][column] <= lowest_score:
				lowest_score = student_grade[row][column]
				lowest_index = f"Student  {row + 1}"
			if student_grade[row][column] >= pass_mark:
				pass_count += 1
			elif student_grade[row][column] < pass_mark:
				fail_count += 1
		print("\n")
		print(f"Highest scoring student in Subject ({column + 1}) is: {highest_index} scoring {highest_score}\n")
		print(f"Lowest scoring student in Subject ({column + 1}) is: {lowest_index} scoring {lowest_score}\n")
		print(f"Total scores in Subject ({column + 1}) is: {subject_total}\n")
		average_subject_score = subject_total / subjects
		print(f"Average score for Subject ({column + 1}) is: {average_subject_score}\n")
		print(f"Pass count for Subject ({column + 1}) is: {pass_count}\n")
		print(f"Fail count for Subject ({column + 1}) is: { fail_count}\n")

def get_overall_calculaion(student_grade, subjects, students):
	overall_highest_score = -1
	overall_highest_index = ""
	overall_lowest_score = sys.maxsize
	overall_lowest_index = ""
	class_total_score = 0
	pass_mark = 50
	overall_pass_count = 0
	overall_fail_count = 0
	overall_pass_count_index = ""
	overall_fail_count_index = ""

	for row in range(students):
		for column in range (subjects):
			score = student_grade[row][column]
			class_total_score += score
			if score > overall_highest_score:
                		overall_highest_score = score;
                		overall_highest_index = f"Student {row + 1} in Subject {column + 1}"
			if score < overall_lowest_score:
				overall_lowest_score = score
				overall_lowest_index = f"Student {row + 1} in Subject {column + 1}"

	for column in range(subjects):
		subject_pass_count  = 0
		subject_fail_count = 0
		for row in range(students):
			if student_grade[row][column] >= pass_mark:
                		subject_pass_count += 1
			elif student_grade[row][column] < pass_mark:
				subject_fail_count += 1
		if subject_pass_count >= overall_pass_count:
			overall_pass_count = subject_pass_count
			overall_pass_count_index = f"Subject {column + 1}"
		if subject_fail_count >= overall_fail_count or overall_fail_count == 0:
			overall_fail_count = subject_fail_count
			overall_fail_count_index = f"Subject {column + 1}"

	class_average_score = class_total_score / (students * subjects)
	print("\n==========================================================================================\n")
	print(f"The hardest subject is {overall_fail_count_index} with {overall_fail_count} failures\n")
	print(f"The easiest subject is {overall_pass_count_index} with {overall_pass_count} passes\n")
	print(f"The overall highest score is scored by {overall_highest_index} scoring {overall_highest_score}\n")
	print(f"The overall lowest score is scored by {overall_lowest_index} scoring {overall_lowest_score}\n")		
	print("\n==========================================================================================\n")
	print("\n")
	print("\n")
	print("CLASS SUMMARY\n")

	print("\n==========================================================================================\n")
	print(f"Best Graduating Student is: {overall_highest_index} scoring {overall_highest_score}\n")
	print("\n")
	print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
	print(f"Worst Graduating Student is: {overall_lowest_index} scoring {overall_lowest_score}\n")
	print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
	print("\n")
	print("\n==========================================================================================\n")
	print(f"Class total score is: {class_total_score}\n")
	print(f"Class Average score is: {class_average_score}\n")
	print("\n==========================================================================================\n")

print("LAGBAJA GROUP OF SCHOOL, LAGOS STATE.\nWELCOME TO THE OFFICIAL GRADING WEBSITE\n")
teacher = input("What is your name,teacher? ")
title = input("Are you a miss, Mr. or Mrs? ")
students = get_student_number(title, teacher)
subjects = get_subjects(title, teacher)
student_grade = [[0] * subjects for _ in range(students)]
get_score(students, subjects, student_grade)
display_table_header(subjects)
display_table_content(student_grade, subjects, students)
print("SUBJECT SUMMARY")
get_subject_calculated(student_grade, subjects, students)
get_overall_calculaion(student_grade, subjects, students)
