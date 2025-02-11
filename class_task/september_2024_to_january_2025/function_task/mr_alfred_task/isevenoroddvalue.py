def even_and_odd_number(numbers):
	result = []
	for i in numbers:
		if i % 2 == 0:
			result.append(True)
		else:
			result.append(False)
	return result
numbers = [10,3,7,1,9,4,2,8,5,6]
print(even_and_odd_number(numbers))

def is_even_or_sum(numbers):
	return[True if i % 2 == 0 else False for i in numbers]
numbers = [10,3,7,1,9,4,2,8,5,6]
print(is_even_or_sum(numbers))


def is_even(value):
	return[x % 2 == 0 for x in value]
value= [10,3,7,1,9,4,2,8,5,6]
print(is_even(value))