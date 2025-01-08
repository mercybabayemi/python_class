def get_vowel_count(words):
	count = 0

	for characters in words:
		if characters == 'a': 
			count += 1
		if characters == 'A': 
			count += 1
		if characters == 'E': 
			count += 1
		if characters == 'e': 
			count += 1
		if characters == 'i': 
			count += 1
		if characters == 'I': 
			count += 1
		if characters == 'O': 
			count += 1
		if characters == 'o': 
			count += 1
		if characters == 'u': 
			count += 1
		if characters == 'U': 
			count += 1
	return count
