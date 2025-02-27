import string
def remove_special_characters(word:str):
    if not type(word):
        raise TypeError
    new_word = ""
    for letter in word:
        if letter not in string.punctuation:
            new_word += letter
    return new_word

print(remove_special_characters("he,ll.o"))