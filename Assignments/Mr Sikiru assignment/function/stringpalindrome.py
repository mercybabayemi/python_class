def is_palindrome(input):
	start_comparison = 0
	stop_comparison = len(input) - 1
	while start_comparison <= stop_comparison:
		if input[start_comparison] != input[stop_comparison]:
 			return False
		start_comparison += 1
		stop_comparison -= 1
	return True