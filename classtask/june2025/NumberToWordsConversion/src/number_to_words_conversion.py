class Conversion:
    def __init__(self):
        self.base_numbers_and_words = {
        1 : "One",
        2 : "Two",
        3 : "Three",
        4 : "Four",
        5 : "Five",
        6 : "Six",
        7 : "Seven",
        8 : "Eight",
        9 : "Nine",
        10 : "Ten",
            11 : "Eleven",
            12 : "Twelve",
            13 : "Thirteen",
            14 : "Fourteen",
            15 : "Fifteen",
            16 : "Sixteen",
            17 : "Seventeen",
            18 : "Eighteen",
            19 : "Nineteen",
            20 : "Twenty",
            30 : "Thirty",
            40 : "Forty",
            50 : "Fifty",
            60 : "Sixty",
            70 : "Seventy",
            80 : "Eighty",
            90 : "Ninety",
            100 : "One Hundred",
            1000 : "One Thousand",
            1000000 : "One million"
    }

    def convert(self, input_string: str):
        num = int(input_string)

        if num in self.base_numbers_and_words:
            return self.base_numbers_and_words[num]
        elif 20 <= num < 99:
            tens = (num // 10) * 10
            units = num % 10
            if units != 0:
                return f"{self.base_numbers_and_words[tens]} {self.base_numbers_and_words[units]}"
            else:
                return self.base_numbers_and_words[tens]
        elif 100 <= num < 999:
            hundreds = (num // 100)
            tens = ((num // 10) % 10) * 10
            units = num % 10
            if units != 0 and tens != 0:
                return f"{self.base_numbers_and_words[hundreds]} Hundred and {self.base_numbers_and_words[tens]} {self.base_numbers_and_words[units]}"
            elif units != 0:
                return f"{self.base_numbers_and_words[hundreds]} Hundred and {self.base_numbers_and_words[units]}"
            elif tens != 0:
                return f"{self.base_numbers_and_words[hundreds]} Hundred and {self.base_numbers_and_words[tens]}"
            else:
                return f"{self.base_numbers_and_words[hundreds]} Hundred"