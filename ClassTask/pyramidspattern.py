input = int(input('Enter number of lines: '))

for row in range(input, 0, -1):
	for column in range(row,0,-1):
		for pattern in range(1,input,-1):
			print(column,pattern, end = '')
	print()
