from players import Players

class Tictactoe:
    def __init__(self, board_capacity = 3):
        self.__board_capacity = board_capacity
        self.__board = [[' ' for i in range(board_capacity)] for i in range(board_capacity)]
        self.__mark_board = ''
        self.__isPlayer = False
        self.__players = Players.PLAYER1
        self.__player_1_marker = 'x'
        self.__player_2_marker = 'o'

    def get_is_players(self):
        return self.__isPlayer

    def get_player(self):
        return self.__players

    def set_is_players(self):
        if not self.get_is_players():
            self.__isPlayer = True
            self.change_players()
        else:
            self.__isPlayer = False
            self.change_players()

    def change_players(self):
        if self.get_player() == Players.PLAYER1:
            self.__players = Players.PLAYER2
        else:
            self.__players = Players.PLAYER1

    def collect_user_preferred_symbol(self, marker):
        if self.get_player() == Players.PLAYER1:
            self.set_player_1_marker(marker)
        elif self.get_player() == Players.PLAYER2:
            self.set_player_2_marker(marker)

    def set_player_1_marker(self, marker):
        self.__player_1_marker = marker

    def set_player_2_marker(self, marker):
        self.__player_2_marker = marker

    def get_player_1_marker(self):
        return self.__player_1_marker

    def get_player_2_marker(self):
        return self.__player_2_marker

    def set_board(self, row, column):
        value = ''
        if not (0 <= row < self.__board_capacity and 0 <= column < self.__board_capacity):
            raise ValueError("Row and column must be within the bounds of the board.")

        if self.get_player() == Players.PLAYER1:
            value = self.get_player_1_marker()
        elif self.get_player() == Players.PLAYER2:
            value = self.get_player_2_marker()

        if self.__board[row][column] == ' ':
            self.__board[row][column] = value
        else:
            raise ValueError(f"Cell at ({row}, {column}) is already occupied.")
        self.set_mark_board()

    def set_mark_board(self):
        flattened = [self.__board[i][j] for i in range(self.__board_capacity) for j in range(self.__board_capacity)]
        self.__mark_board = (
            f" {flattened[0]} | {flattened[1]} | {flattened[2]} \n"
            f"-----------\n"
            f" {flattened[3]} | {flattened[4]} | {flattened[5]} \n"
            f"-----------\n"
            f" {flattened[6]} | {flattened[7]} | {flattened[8]} \n"
        )

    def get_mark_board(self):
        return self.__mark_board

    def get_board(self):
        return self.__board