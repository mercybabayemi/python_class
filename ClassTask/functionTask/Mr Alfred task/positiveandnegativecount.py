def get_index_positive_count(input):
	positive_count = 0
	for item in input:
		if item > 0:
			positive_count += 1
	return positive_count

def get_index_negative_count(input):
	negative_count = 0
	for item in input:
		if item < 0:
			negative_count += 1
	return negative_count
	