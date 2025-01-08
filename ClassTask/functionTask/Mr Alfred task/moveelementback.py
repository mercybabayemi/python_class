def get_element_movement(x,y):
	x = [1,2,3,4,5]
	y = 2
	main_number = x
	x = x[0:y]
	main_number = main_number[y: ]
	main_number.extend(x)
	return main_number