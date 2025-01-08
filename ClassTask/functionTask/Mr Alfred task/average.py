def get_list_average(numbers):
	count = 0
	total = 0
	for i in numbers:
		total += i
		count += 1

	average = total // count
	return average