def elementOccurance(numbers:list,element:int):
	for item in numbers:
		if item == element:
			return "Element exist in list at index"
	return "Element does not exist at index"
		