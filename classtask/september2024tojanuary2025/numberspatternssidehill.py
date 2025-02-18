input = int(input('Enter number: '))

for row in range(1,input +1):
	for column in range(1,row +1):
		print(column, end = ' ')
	print()
for row in range(1,input, +1):
	for repeat in range(1,(input +1) - row):
		print(repeat, end = ' ')
	print()

