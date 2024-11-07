count = 0
passed = 0
failed = 0
while count <= 14:
	scores = int(input('Enter student grade: '))
	count += 1
	if scores >= 45:
		passed += 1
		print('Student who passed are ', passed )
	if scores  < 45:
		failed += 1
		print('Student who failed are ', failed )

print('The total number of students who failed are ', failed)
print('The total number of students who passed are ', passed)