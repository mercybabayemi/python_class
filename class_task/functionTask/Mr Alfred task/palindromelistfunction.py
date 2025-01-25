def get_is_palindrome(words:list):
	return[True if item == item[::-1] else False for item in words]

list((map(lambda word: word==word[::-1], words)))
