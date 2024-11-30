def zip_function_sample(keys:list,values:list):
	new_value = {}
	for key,value in zip(keys,values):
		new_value[key] = value
	return new_value
