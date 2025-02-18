import random

from string import ascii_letters, punctuation, digits

class Generator:
    def __init__(self):
        self._password = ""

    def get_password(self):
        return self._password

    def generate_random_number_letters_and_punctuation(self):
        represent = ascii_letters + digits + punctuation
        return random.choice(represent)

    def set_password(self):
        for i in range(0,16):
            returned = self.generate_random_number_letters_and_punctuation()
            self._password += returned


