def odd_position_numbers(numbers:list):
	odd_position = []	
	for item in numbers:
		if item % 2 != 0:
			odd_position.append(item)
	return odd_position
