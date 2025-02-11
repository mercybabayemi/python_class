def get_string_anagram(first_word,second_word):
	for character in first_word:
		if character in second_word:
			return True
		else:
			return False