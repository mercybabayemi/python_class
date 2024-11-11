def get_acronym(word):
	acronym = " "
	letters = user_input.strip()
	for alphabet in letters:
		acronym += letters[0]
		print(letters)
		print(alphabet)
		return acronym

user_input = input("Enter words: ")
print(get_acronym(user_input))

"""
Write a function that takes a string and
returns the acronym of the string.
Example:
Input : "Portable Network Graphics"
Output: PNG
"""
