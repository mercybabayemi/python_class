for integer in range(3):
	integer = int(input('Enter a non negative digit integer: '))
	factorial = 1
	while integer > 0:
		factorial = factorial * integer
		integer = integer - 1

print(factorial)
