def get_dictionary_value_squared(num):
    my_dict = {}
    keys = []
    values = []
    for each in range(1, 3):
        keys.append(each)
        if each == 1:
            val = num * each
        if each == 2:
            val = num * num
        values.append(val)

    for key, value in zip(keys, values):
        my_dict[key] = value
    return my_dict
