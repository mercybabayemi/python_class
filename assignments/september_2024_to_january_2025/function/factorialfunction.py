def factorial_of(integer):
	if integer < 0:
		return ValueError("Factorial is not defined for negative numbers")
	elif integer == 0 or integer == 1:
		return 1
	else:
		result = 1
		for item in range(1, integer + 1):
			result *= item
		return result