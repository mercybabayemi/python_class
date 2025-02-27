def get_character_frequency(word):
    try:
        empty_dict = {}
        for letter in word:
            if letter in empty_dict:
                empty_dict[letter] += 1
            else:
                empty_dict[letter] = 1
        return empty_dict
    except TypeError:
        print("object is not iterable")


print(get_character_frequency('semicolon.africa'))