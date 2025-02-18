def get_sum_of_odd_digits(numbers):
	total = 0
	sum_list = []
	for i in [1,2,3,4,5]:
		sum_list.append(numbers)
		if i % 2 != 0:
			total += i
	return total