def encrypt_text(text):
    encrypted = ""
    for letter in text:
        if letter.isalpha():
            base = "a" if letter.islower() else "A"
            encrypted_char_calculated = (ord(letter) - ord(base) + 13) % 26 + ord(base)
            encrypted_char = chr(encrypted_char_calculated)
            encrypted += encrypted_char
        elif letter.isdigit():
            base = "0"
            encrypted_char_calculated = (ord(letter) - ord(base) + 13) % 10 + ord(base)
            encrypted_char = chr(encrypted_char_calculated)
            encrypted += encrypted_char
        else:
            symbol_range = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
            if letter in symbol_range:
                symbol_index = symbol_range.index(letter)
                new_symbol_index = (symbol_index + 5) % len(symbol_range)
                encrypted += symbol_range[new_symbol_index]
            else:
                encrypted += letter

    return encrypted

print(encrypt_text("Mercy 12 .3"))
