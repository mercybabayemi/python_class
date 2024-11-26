def is_palindrome(integer):
	reversed = 0
	original = integer
	digit = 0
	while integer != 0:
		digit = integer % 10
		reversed = reversed * 10 + digit
		integer //= 10

	return original == reversed

		