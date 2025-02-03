def get_prime_number(numbers):
	if numbers == 2:
		return True
	if number <= 2:
		return false
	if number % 2 == 0:
		return false

	for number in range(3,numbers-1):
		if numbers % number == 0:
			return False
	return True
