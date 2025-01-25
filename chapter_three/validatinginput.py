passes = 0
failures = 0

for students in range(10):
	result = int(input("Enter result(1 for pass,2 for fail): "))

	if result == 1:
		passes = passes + 1 
	elif result == 2:
		failures = failures + 1
	else: 
		print("Try again")

print("Passed: ", passes)
print("Failed: ", failures)

if passes > 8:
	print("Bonus to instructor")