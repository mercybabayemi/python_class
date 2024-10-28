user_input = input("Enter a single alphabet: ")
A = 'A'
a = 'a'
E = 'E'
e = 'e'
I = 'I'
i = 'i'
O = 'O'
o = 'o'
U = 'U'
u = 'u'
if len(user_input) == 1 and user_input.isalpha():
    if user_input  == A:
      print("Letter Input is a vowel")
    elif user_input == a:
      print("Letter Input is a vowel")
    elif user_input == E:
      print("Letter Input is a vowel")
    elif user_input == e:
      print("Letter Input is a vowel")
    elif user_input == I:
      print("Letter Input is a vowel")
    elif user_input == i:
      print("Letter Input is a vowel")
    elif user_input == O:
      print("Letter Input is a vowel")
    elif user_input == o:
      print("Letter Input is a vowel")
    elif user_input == U:
      print("Letter Input is a vowel")
    elif user_input == u:
      print("Letter Input is a vowel")
    else:
      print("Letter Input is a consonant")
else:
      print("Error Message")