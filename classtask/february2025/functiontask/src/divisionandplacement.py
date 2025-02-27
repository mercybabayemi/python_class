def get_place(word:str, second_word):
    try:
        new_word = ""
        even = len(word)//2
        if len(word) % 2 == 0:
            first_part = word[:even]
            second_part = word[even:]
            new_word = first_part + second_word + second_part
        else:
            new_word = word + second_word
        return new_word
    except TypeError:
        print("object is not iterable")


print(get_place("helllo", "ce"))
print(get_place("joy", "ce"))