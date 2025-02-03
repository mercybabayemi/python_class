##pass an integer and go through the range to print a list
def populate_task_list_comprehension(number):
	return[i for i in range(1,number)]
print(populate_task_list_comprehension(5))


##pass no argument to print integer sum from range
def populate_task_list_sum():
	return(sum([i for i in range(1,5)]))
print(populate_task_list_sum())


##pass a list to return an int
def total(number:list):
	total = 0
	for each_number in number:
		total += each_number
	return total


##pass no argument to loop through integer range and return list
def populate_task_list_total():
	return(total([i for i in range(1,6)]))
print(populate_task_list_total())


##pass int, loop through int range and return list
def get_cube(number):
	cube = []
	for each_number in range(1,number):
		cube.append(each_number ** 3)
	return cube
print(get_cube(6))


def get_cube_second_trial(number:list):
	cube = []
	for each in number:
		cube.append(each ** 3)
	return cube
print(get_cube_second_trial([1,2,3,4,5]))


##pass an integer and return range
def individual_number(number):
	return[i for i in range(number)]
print(individual_number(10))


##pass a list and return each element in number
def individual_number_two(number:list):
	return[i for i in number]
print(individual_number_two([1,2,3]))
print(individual_number_two([6]))


##pass int number and loop through range
def populate_list(number):
	return[i for i in range(1,number)]
print(populate_list(5))


##pass no arguement and loop through range of int to return int
def populate_task_list_sum():
	return(sum([i for i in range(1,6)]))
print(populate_task_list_sum())


##pass list and list function and return a list  
def get_cube(numbers:list):
	return[(i**3) for i in numbers]
print(get_cube([5,6,7,8,9,10]))
print(get_cube(populate_list(6)))

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

def string_capitalize(words):
	return [word.capitalize() for word in words]
words = ['orange','red']
print(string_capitalize(words))
