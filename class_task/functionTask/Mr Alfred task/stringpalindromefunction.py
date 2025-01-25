def get_string_palindrome(word):
	
	reverse = " "

	comparator = word[-1]
	
	for character in word:
		reverse += comparator
		
	if word == reverse:
		return True
	else:
		return False