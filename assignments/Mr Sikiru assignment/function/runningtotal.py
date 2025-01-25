def running_total_computed(numbers:list):
	total = 0;
	for item in numbers:
		total += item
		print(f"Running sum is currently {total}\n")
	return total
