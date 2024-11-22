def find_duplicate(numbers):
	for i in numbers:
		for j in numbers:
			if i == j:
				return True
			else:
				return False