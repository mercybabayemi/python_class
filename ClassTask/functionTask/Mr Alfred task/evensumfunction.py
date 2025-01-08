def is_even(numbers):
	sum = 0
	for number in numbers:
		if number % 2 == 0:
			sum += number
	return sum