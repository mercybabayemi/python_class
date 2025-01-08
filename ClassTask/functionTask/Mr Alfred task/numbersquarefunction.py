def get_number_square(user_input):
	return[each*each for each in range(1,user_input)]

user_input = 5
print(list(map(lambda each: each*each, range(1, user_input))))