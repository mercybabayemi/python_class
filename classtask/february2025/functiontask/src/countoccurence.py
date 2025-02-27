def get_count_occurrence(word, letter):
    try:
        word_tuple = tuple(word)
        number = word_tuple.count(letter)
        new_word = [letter, number]
        update = tuple(new_word)
        return update
    except TypeError:
        print("object is not iterable")

print(get_count_occurrence("semicolon", "o"))
