def get_sorted_mixed_case_words(word: str):
    if not type(word):
        raise TypeError
    upper_case = " "
    lower_case = " "
    others = " "
    for letter in word:
        if letter.isupper():
            upper_case += letter
        elif letter.islower():
            lower_case += letter
        else:
            others += letter

    new_word = upper_case + lower_case + others

    return  new_word.replace(" ", "")

print(get_sorted_mixed_case_words("sEmIC1o2lOn"))
