def get_student_grade(student_scores):
    grades = []
    for score in student_scores.values():
        if score >= 90 and score <= 100:
            grade = "Outstanding"
            grades.append(grade)
        if score >= 81 and score <= 90:
            grade = "Exceeds Expectations"
            grades.append(grade)
        if score >= 71 and score <= 80:
            grade = "Acceptable"
            grades.append(grade)
        if score  <= 70:
            grade = "Fail"
            grades.append(grade)
    return grades

