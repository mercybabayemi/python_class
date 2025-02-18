def populate_task_list_comprehension(number):
	return[i for i in range(1,number)]


print(populate_task_list_comprehension(5))

def populate_task_list_sum():
	return(sum([i for i in range(1,5)]))

print(populate_task_list_sum())



def total(number:list):
	total = 0
	for each_number in number:
		total += each_number
	return total



def populate_task_list_total():
	return(total([i for i in range(1,6)]))

print(populate_task_list_total())

