def encrypt_text(text):
    encrypted = ""
    for word in text:
        for letter in word:
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
                base = "1"
                encrypted += letter
    return encrypted

