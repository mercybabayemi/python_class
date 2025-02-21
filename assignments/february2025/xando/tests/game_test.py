import unittest

from game import Game
from players import Players


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game1 = Game()

    def test_that_game_has_a_board_and_it_is_empty(self):
        expecting = [[None for i in range(3)] for i in range(3)]
        self.assertListEqual(expecting, self.game1.get_board())

    def test_that_game_has_players_and_it_switches(self):
        self.assertFalse(self.game1.get_is_players())
        self.assertEqual(Players.PLAYER1, self.game1.get_player())
        self.game1.set_is_players()
        self.assertTrue(self.game1.get_is_players())
        self.assertEqual(Players.PLAYER2, self.game1.get_player())
        self.game1.set_is_players()
        self.assertFalse(self.game1.get_is_players())
        self.assertEqual(Players.PLAYER1, self.game1.get_player())

    def test_that_players_choose_Characters(self):
        self.assertFalse(self.game1.get_is_players())
        self.assertEqual(Players.PLAYER1, self.game1.get_player())
        self.game1.collect_user_preferred_symbol('x')
        self.assertEqual('x',self.game1.get_player_1_marker())
        self.game1.set_is_players()
        self.assertTrue(self.game1.get_is_players())
        self.assertEqual(Players.PLAYER2, self.game1.get_player())
        self.game1.collect_user_preferred_symbol('o')
        self.assertEqual('o', self.game1.get_player_2_marker())

    def test_that_players_markers_are_entered_in_board(self):
        self.assertFalse(self.game1.get_is_players())
        self.game1.collect_user_preferred_symbol('x')
        self.game1.set_is_players()
        self.assertTrue(self.game1.get_is_players())
        self.game1.collect_user_preferred_symbol('o')
        self.game1.set_board(0,0)
        self.game1.set_is_players()
        self.game1.set_board(0, 1)
        self.game1.set_is_players()
        self.game1.set_board(0, 2)
        self.game1.set_is_players()
        self.game1.set_board(1, 0)
        self.game1.set_is_players()
        self.game1.set_board(1, 1)
        self.game1.set_is_players()
        self.game1.set_board(1, 2)
        self.game1.set_is_players()
        self.game1.set_board(2, 0)
        self.game1.set_is_players()
        self.game1.set_board(2, 1)
        self.game1.set_is_players()
        self.game1.set_board(2, 2)
        self.game1.set_is_players()
        expecting = [['o','x','o'],['x','o','x'],['o','x','o']]
        self.assertListEqual(expecting ,self.game1.get_character_board())

    def test_that_players_markers_entered_in_board_throws_exception_when_position_is_occupied(self):
        self.assertFalse(self.game1.get_is_players())
        self.game1.collect_user_preferred_symbol('x')
        self.game1.set_is_players()
        self.assertTrue(self.game1.get_is_players())
        self.game1.collect_user_preferred_symbol('o')
        self.game1.set_board(0,0)
        self.game1.set_is_players()
        with self.assertRaises(ValueError):
            self.game1.set_board(0, 0)

    def test_that_players_markers_entered_in_board_throws_exception_when_column_is_out_of_bound(self):
        self.assertFalse(self.game1.get_is_players())
        self.game1.collect_user_preferred_symbol('x')
        self.game1.set_is_players()
        self.assertTrue(self.game1.get_is_players())
        self.game1.collect_user_preferred_symbol('o')
        with self.assertRaises(ValueError):
            self.game1.set_board(4, 0)

    def test_test_players_markers_are_entered_in_board_and_displays_binary_when_completed(self):
        self.assertFalse(self.game1.get_is_players())
        self.game1.collect_user_preferred_symbol('x')
        self.game1.set_is_players()
        self.assertTrue(self.game1.get_is_players())
        self.game1.collect_user_preferred_symbol('o')
        self.game1.set_board(0, 0)
        self.game1.set_is_players()
        self.game1.set_board(0, 1)
        self.game1.set_is_players()
        self.game1.set_board(0, 2)
        self.game1.set_is_players()
        self.game1.set_board(1, 0)
        self.game1.set_is_players()
        self.game1.set_board(1, 1)
        self.game1.set_is_players()
        self.game1.set_board(1, 2)
        self.game1.set_is_players()
        self.game1.set_board(2, 0)
        self.game1.set_is_players()
        self.game1.set_board(2, 1)
        self.game1.set_is_players()
        self.game1.set_board(2, 2)
        self.game1.set_is_players()
        expecting = [[0, 1 , 0], [1, 0, 1], [0, 1, 0]]
        self.assertListEqual(expecting, self.game1.get_binary_board())

if __name__ == '__main__':
    unittest.main()
