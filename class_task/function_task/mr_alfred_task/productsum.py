def get_product_sum(numbers):
	sum = 0
	product = 1
	for i in numbers:
		product = i * i
		sum += product
	return sum