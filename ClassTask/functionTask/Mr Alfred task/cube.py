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


##pass list and list function and return a list  
def get_cube(numbers:list):
	return[(i**3) for i in numbers]
print(get_cube([5,6,7,8,9,10]))
print(get_cube(populate_list(6)))