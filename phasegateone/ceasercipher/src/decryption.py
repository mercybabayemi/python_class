from src.encryption import encrypt_text


def decrypt_text(text):
    decrypted = ""
    for letter in text:
        if letter.isalpha():
            base = "a" if letter.islower() else "A"
            decrypted_char_calculated = (ord(letter) - ord(base) - 13) % 26 + ord(base)
            decrypted_char = chr(decrypted_char_calculated)
            decrypted += decrypted_char
        elif letter.isdigit():
            base = "0"
            decrypted_char_calculated = (ord(letter) - ord(base) - 13) % 10 + ord(base)
            decrypted_char = chr(decrypted_char_calculated)
            decrypted += decrypted_char
        else:
            symbol_range = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
            if letter in symbol_range:
                symbol_index = symbol_range.index(letter)
                new_symbol_index = (symbol_index - 5) % len(symbol_range)  # Reverse the shift by 5
                decrypted += symbol_range[new_symbol_index]
            else:
                decrypted += letter

    return decrypted

encrypted_text = encrypt_text("Mercy 12 .3")
decrypted_text = decrypt_text(encrypted_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
