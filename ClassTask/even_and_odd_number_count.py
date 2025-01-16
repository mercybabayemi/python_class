def get_odd_and_even_number_count(numbers):
	even_count = 0
	odd_count = 0
	new_list = []
	for each in numbers:
		if each % 2 != 0:
			odd_count += 1
		if each % 2 == 0:
			even_count += 1
	new_list.append(odd_count)
	new_list.append(even_count)
	return new_list

numbers_1 =[1,2,3,6,8,10]
numbers_2 = [5,3,7,9,2,8]
print(get_odd_and_even_number_count(numbers_1))
print(get_odd_and_even_number_count(numbers_2))