def is_palindrome(input):
	start_comparison = input
	stop_comparison = len(input) - 1
	while start_comparison < stop_comparison:
		for item in input:
			for element in len(input) - 1:
				if item != element:
 					return False
		start_comparison += 1
		stop_comparison -= 1

	return True