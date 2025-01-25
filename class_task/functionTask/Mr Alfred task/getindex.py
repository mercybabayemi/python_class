def get_index(input, search):
	count = 0
	for item in input:
		count += 1
		if item == search:
			return count - 1
	return "not available"
