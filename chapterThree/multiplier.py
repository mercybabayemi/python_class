for number in range(1, 13, 1):
	for multiplier in range(2, 21, 1):
		result = multiplier * number
		print(multiplier, '*', number , '=', result , end = '\t')
	print(' ')