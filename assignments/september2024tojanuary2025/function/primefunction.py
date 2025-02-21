def is_prime_number(integer):
	if integer <= 2:
		return False

	if integer == 2:
		return True

	if integer % 2 == 0:
		return False

	else:
		for item in range(3,integer-1):
			if integer % item == 0:
				return False
	return True
