##pass int number and loop through range
def populate_list(number):
	return[i for i in range(1,number)]
print(populate_list(5))

#pass a list and return a list
def get_even(numbers):
	return[i for i in numbers if i % 2 == 0]
print(get_even([1,2,3,4,5]))
print(get_even(populate_list(15)))

##pass a list to return an int
def total(number:list):
	total = 0
	for each_number in number:
		total += each_number
	return total


def get_even_count_one(numbers):
	return len(get_even_count_one(populate_list(10)))



def get_even_count_two(numbers):
	return sum([1 for i in numbers if i % 2 == 0 ])
print("Even number first count = ", get_even_count_two([1,2,3,4,5]))
print("Even number second count = ", get_even_count_two(populate_list(15)))


def even_and_odd_number(numbers):
	for i in numbers:
		if i % 2 == 0:
			return True
		else:
			return False
numbers = [10,3,7,1,9,4,2,8,5,6]
print(even_and_odd_numbers(numbers))

def is_even_or_sum(numbers):
	return [True for i in numbers if i % 2 == 0 else return False]
numbers = [10,3,7,1,9,4,2,8,5,6]
print(is_even_or_sum(numbers))


