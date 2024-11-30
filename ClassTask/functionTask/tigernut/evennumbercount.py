#pass a list and return a list
def get_even(numbers):
	return[i for i in numbers if i % 2 == 0]
print(get_even([1,2,3,4,5]))
print(get_even(populate_list(15)))


##ass a list and return a list
def get_even_sum(numbers):
	return(sum([i for i in numbers if i % 2 == 0]))
print(get_even_sum([1,2,3,4,5]))
print(get_even_sum(populate_list(15)))


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