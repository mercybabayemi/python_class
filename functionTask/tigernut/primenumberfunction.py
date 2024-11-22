def get_prime_number(numbers):
	if numbers == 2 and numbers % 2 == 0:
		return True

	for number in range(3,numbers):
		if numbers % number == 0:
			return False
		elif numbers % 2 == 0:
			return False
		else: 
			return True
