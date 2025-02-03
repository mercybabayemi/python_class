def get_even_number(message):
	even = []
	for each in message:
		if each.isdigit():
			num = int(each)
			if num % 2 == 0:
				even.append(num)
		else:
			pass
	return even