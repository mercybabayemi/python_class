class SevenSegmentDisplay:
    def __init__(self):
        self._is_on = False
        self.__board_capacity = 4
        self.__board = [[' ' for i in range(self.__board_capacity)] for i in range(self.__board_capacity + 1)]

    def get_is_on(self):
        return self._is_on

    def get_board(self):
        return self.__board

    def display_segment(self, digits):
        self.validate(digits)
        value = self.change_status(digits)
        if value:
            self.set_board(digits)
        return self.get_board()

    def change_status(self, digits):
        if digits[7] == '1':
            self._is_on = True
            return self.get_is_on()
        else:
            self._is_on = False
            return self.get_is_on()

    def set_board(self, digits):

        if digits[0] == '1':
            for i in range(4):
                self.__board[0][i] = "#"
            # self.__board[0][0] = '#'
            # self.__board[0][1] = '#'
            # self.__board[0][2] = '#'
            # self.__board[0][3] = '#'

        if digits[1] == '1' and digits[2] == '1':
            self.__board[1][3] = '#'
            self.__board[2][3] = '#'
            self.__board[3][3] = '#'
        elif digits[1] == '1':
            self.__board[1][3] = '#'
            self.__board[2][3] = '#'
        elif digits[2] == '1':
            self.__board[2][3] = '#'
            self.__board[3][3] = '#'

        if digits[3] == '1':
            self.__board[4][0] = '#'
            self.__board[4][1] = '#'
            self.__board[4][2] = '#'
            self.__board[4][3] = '#'

        if digits[4] == '1' and digits[5] == '1':
            self.__board[1][0] = '#'
            self.__board[2][0] = '#'
            self.__board[3][0] = '#'
        elif digits[1] == '1':
            self.__board[1][0] = '#'
            self.__board[2][0] = '#'
        elif digits[2] == '1':
            self.__board[2][0] = '#'
            self.__board[3][0] = '#'

        if digits[6] == '1':
            self.__board[2][0] = '#'
            self.__board[2][1] = '#'
            self.__board[2][2] = '#'
            self.__board[2][3] = '#'

    def validate(self, digits):
        if not digits.isdigit():
            raise ValueError("Binary number must be only digits")
        if not all(digit in '01' for digit in digits):
            raise ValueError("Binary number must consist of only 0s and 1s")
        if len(digits) != 8:
            raise ValueError("Binary number must be 8 digits long")


if __name__ == "__main__":
    display = SevenSegmentDisplay()
    print(display.display_segment("11111101"))
    print(display.display_segment("01100001"))
    print(display.display_segment("11011011"))
    print(display.display_segment("11110011"))

