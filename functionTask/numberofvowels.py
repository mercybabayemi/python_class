
"""
write a function that takes a string and return the number of vowels in the string.
"""

def get_vowels(words):
	vowels = "AEIOUaeiou"
	vowels_count = 0
	for character in words:
		if character in vowels:
			vowels_count = vowels_count + 1
	return vowels_count

letters = input("Enter a word: ")
print(get_vowels(letters))