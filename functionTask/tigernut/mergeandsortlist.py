def get_merged_and_sorted_list(input_one, input_two):
	input_one.extend(input_two)
	return sorted(input_one)
	