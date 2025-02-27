def swap_and_convert_characters(first_word, second_word):
    if not type(first_word) or not type(second_word):
        raise TypeError
    first_word_last = first_word[-1]
    second_word_last = second_word[-1]

    first_word = first_word[:-1] + second_word_last
    second_word = second_word[:-1] + first_word_last

    joined = " ".join([second_word,first_word])
    return joined


print(swap_and_convert_characters('abc','def'))