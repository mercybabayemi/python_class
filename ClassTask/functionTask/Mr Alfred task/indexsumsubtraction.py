def get_index_sum(numbers):
	total = 0
	final = 0
	for i in numbers:
		for j in numbers:
			final += j
		final = final - i
	return final
