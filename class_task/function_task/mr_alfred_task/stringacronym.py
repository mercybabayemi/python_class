def get_string_acronym(word):
	acronym = ""
	splitted = word.split()
	for item in splitted:
		acronym += item[0]
	return acronym