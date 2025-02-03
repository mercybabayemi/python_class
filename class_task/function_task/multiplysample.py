def multiply(first,second):
	for index in range(second):
		print(index * first, end = " ")
	print()

def times_table(third):
	for index in range(third):
		multiply(index,5)
	print()
times_table(10)