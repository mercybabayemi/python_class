def get_factorial(number):
	factorial = 1
	for i in range(1, number+1):
		factorial *= i
	return factorial