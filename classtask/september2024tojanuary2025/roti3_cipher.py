def encrypt_text(text):
    encrypted = ""
    for letter in text:
            if letter.isalpha():
                base = "a"
                if letter.islower():
                    base = "a"
                elif letter.isupper():
                    base = "A"
                encrypted_char_calculated = (ord(letter) - ord(base) + 13 + 26)% 26 + ord(base)
                encrypted_char = chr(encrypted_char_calculated)
                encrypted += encrypted_char
            elif letter.isdigit():
                base = "0"
                encrypted_char_calculated = (ord(letter) - ord(base) + 13 + 10)% 10 + ord(base)
                encrypted_char = chr(encrypted_char_calculated)
                encrypted += encrypted_char
            else:
                encrypted += letter

    return encrypted

print(encrypt_text("Mercy 12 .3"))