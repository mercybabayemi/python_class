def encrypt_text(text):
    encrypted = ""
    for word in text:
        for letter in word:
            if letter.isalpha():
                base = "a"
                if base.islower():
                    base = "a"
                elif base.isupper():
                    base = "A"
                encrypted_char_calculated = (ord(letter) - ord(base) + 13 + 26)% 26 + ord(base)
                encrypted_char = chr(encrypted_char_calculated)
                encrypted += encrypted_char
            else:
                encrypted += letter
    return encrypted

