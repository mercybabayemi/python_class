input= int(input('Enter a number: '))

for row in range(input, 0, - 1):
	for column in range(row,0, - 1):
		print(column ,end = ' ')
	print()