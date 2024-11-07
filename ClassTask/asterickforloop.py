input = (int(input('Enter a number: ')))

for row in range(1, input + 1):
	for column in range(1, row + 1):
		print('*',end = ' ')
	print()