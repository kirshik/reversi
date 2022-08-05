import unittest

from model.board import Board
from model.players import Player
from model.game import Game


class TestGame(unittest.TestCase):

    def test_put_started_disks(self):
        board_4 = Board(4)
        board_8 = Board(8)
        board_7 = Board(7)

        game_4 = Game(board_4)
        game_8 = Game(board_8)
        game_7 = Game(board_7)

        game_4.put_started_disks()
        game_8.put_started_disks()
        game_7.put_started_disks()

        # Check game_4
        self.assertEqual(board_4.get_cell(1, 1), Player.X)
        self.assertEqual(board_4.get_cell(2, 2), Player.X)
        self.assertEqual(board_4.get_cell(1, 2), Player.O)
        self.assertEqual(board_4.get_cell(2, 1), Player.O)

        # Check game_8
        self.assertEqual(board_8.get_cell(3, 3), Player.X)
        self.assertEqual(board_8.get_cell(4, 4), Player.X)
        self.assertEqual(board_8.get_cell(3, 4), Player.O)
        self.assertEqual(board_8.get_cell(4, 3), Player.O)

        # Check game_7
        self.assertEqual(board_7.get_cell(3, 3), Player.X)
        self.assertEqual(board_7.get_cell(2, 2), Player.X)
        self.assertEqual(board_7.get_cell(3, 2), Player.O)
        self.assertEqual(board_7.get_cell(2, 3), Player.O)

    def test_change_player(self):
        board = Board(8)
        game = Game(board)

        # testing initial player, then switch to Plater.O and Player.X
        self.assertEqual(game.curr_player, Player.X)
        game.change_player()
        self.assertEqual(game.curr_player, Player.O)
        game.change_player()
        self.assertEqual(game.curr_player, Player.X)

    def test_is_valid_move_positive_cases(self):
        board = Board(4)
        game = Game(board)
        game.put_started_disks()

        # Player X row and column moves
        self.assertTrue(game.is_valid_move(1, 3))
        self.assertTrue(game.is_valid_move(3, 1))

        game.change_player()
        # Player O row and column moves
        self.assertTrue(game.is_valid_move(3, 2))
        self.assertTrue(game.is_valid_move(2, 3))

        game.make_move(3, 2)
        game.change_player()
        # Player X diagonals
        self.assertTrue(game.is_valid_move(3, 3))
        game.make_move(3, 3)
        game.change_player()
        game.make_move(1, 0)
        game.change_player()
        self.assertTrue(game.is_valid_move(0, 0))

        # Player O diagonals
        game.make_move(0, 2)
        game.change_player()

        self.assertTrue(game.is_valid_move(0, 3))

        board = Board(4)
        game = Game(board)
        game.put_started_disks()
        game.make_move(2, 0)
        game.change_player()

        self.assertTrue(game.is_valid_move(3, 0))

    def test_is_valid_move_negative_cases(self):
        board = Board(4)
        game = Game(board)
        game.put_started_disks()

        # test cells outside the board
        self.assertFalse(game.is_valid_move(-1, 5))
        self.assertFalse(game.is_valid_move(3, 5))

        # test cells which don't turn over other player disks
        self.assertFalse(game.is_valid_move(0, 0))
        self.assertFalse(game.is_valid_move(3, 3))

        # test cells occupied by other player, but valid to current player
        game.make_move(2, 0)
        game.change_player()
        game.make_move(3, 0)
        game.change_player()
        game.make_move(1, 3)
        self.assertFalse(game.is_valid_move(0, 2))

        # test cell occupied by current player
        self.assertFalse(game.is_valid_move(0, 2))

    def test_make_move(self):
        board = Board(4)
        game = Game(board)
        game.put_started_disks()

        game.make_move(2, 0)

        # test flipping other player disks
        self.assertEqual(board.get_cell(2, 0), Player.X)
        self.assertEqual(board.get_cell(2, 2), Player.X)
        self.assertEqual(board.get_cell(2, 1), Player.X)

        # test invalid move
        self.assertIsNone(game.make_move(0, 0))

        # test flipping diagonal disks
        game.change_player()
        game.make_move(3, 0)
        self.assertEqual(board.get_cell(3, 0), Player.O)
        self.assertEqual(board.get_cell(2, 1), Player.O)
        self.assertEqual(board.get_cell(1, 2), Player.O)

    def test_is_terminated_positives_cases(self):
        board = Board(4)
        game = Game(board)

        # fill board with disks
        for i in range(4):
            for j in range(4):
                if j % 2 == 0:
                    board.update_cell(i, j, Player.X)
                else:
                    board.update_cell(i, j, Player.O)

        # test full board
        self.assertTrue(game.is_terminated())

        # fill board with X player disks
        for i in range(4):
            for j in range(4):
                if j % 2 == 0:
                    board.update_cell(i, j, Player.X)
                else:
                    board.update_cell(i, j, board.EMPTY_CELL)

        # test X player occupied all board
        self.assertTrue(game.is_terminated())

        # fill board with O player disks
        for i in range(4):
            for j in range(4):
                if j % 2 == 0:
                    board.update_cell(i, j, Player.O)
                else:
                    board.update_cell(i, j, board.EMPTY_CELL)

        # test O player occupied all board
        self.assertTrue(game.is_terminated())

        # test no valid move case
        for i in range(4):
            for j in range(4):
                if (i == 0 and j == 3) or (i == 1 and j == 3):
                    board.update_cell(i, j, Player.X)
                elif (i == 2 and j == 3) or (i == 3 and j == 3):
                    board.update_cell(i, j, board.EMPTY_CELL)
                else:
                    board.update_cell(i, j, Player.O)

        self.assertTrue(game.is_terminated())

    def test_is_terminated_negatives_cases(self):
        board = Board(4)
        game = Game(board)
        game.put_started_disks()

        # test start of game terminality
        self.assertFalse(game.is_terminated())

        # test midle game case
        game.make_move(2, 0)
        self.assertFalse(game.is_terminated())

        # test one player have no moves
        for i in range(4):
            for j in range(4):
                if (i == 3 and j == 0) or (i == 1 and j == 3) or (i == 2 and j == 3) or (i == 3 and j == 3):
                    board.update_cell(i, j, board.EMPTY_CELL)
                elif i == 0 and j == 3:
                    board.update_cell(i, j, Player.X)
                else:
                    board.update_cell(i, j, Player.O)

        self.assertFalse(game.is_terminated())
