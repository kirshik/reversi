import unittest
from model.board import Board
from model.players import Player
from exceptions.invalid_board_size_error import InvalidBoardSizeError


class TestBoard(unittest.TestCase):

    def test_is_inside_positive_cases(self):
        board = Board(4)
        self.assertTrue(board.is_inside(0, 0))
        self.assertTrue(board.is_inside(3, 3))
        self.assertTrue(board.is_inside(0, 3))
        self.assertTrue(board.is_inside(3, 0))
        self.assertTrue(board.is_inside(2, 2))

    def test_is_inside_negative_cases(self):
        board = Board(4)
        self.assertFalse(board.is_inside(-1, 0))
        self.assertFalse(board.is_inside(0, -1))
        self.assertFalse(board.is_inside(4, 0))
        self.assertFalse(board.is_inside(0, 4))
        self.assertFalse(board.is_inside(5, 5))
        self.assertFalse(board.is_inside(5, 1))
        self.assertFalse(board.is_inside(1, 5))
        self.assertFalse(board.is_inside(3, 10))

    def test_is_full_positive_cases(self):
        board_different_players = Board(4)
        board_o_player = Board(4)
        board_x_player = Board(4)
        big_board_o_player = Board(100)

        # fill board with different players
        for i in range(4):
            for j in range(4):
                if (i+j) % 3 == 0:
                    board_different_players.update_cell(i, j, Player.O)
                else:
                    board_different_players.update_cell(i, j, Player.X)

        # fill board with O player
        for i in range(4):
            for j in range(4):
                board_o_player.update_cell(i, j, Player.O)

        # fill board with X player
        for i in range(4):
            for j in range(4):
                board_x_player.update_cell(i, j, Player.X)

        # fill big board with O player
        for i in range(100):
            for j in range(100):
                big_board_o_player.update_cell(i, j, Player.O)

        # test cases
        self.assertTrue(board_different_players.is_full())
        self.assertTrue(board_o_player.is_full())
        self.assertTrue(board_x_player.is_full())
        self.assertTrue(big_board_o_player.is_full())

    def test_is_full_negative_cases(self):
        board_almost_full_with_o_player = Board(4)
        board_almost_full_with_x_player = Board(4)
        board_empty = Board(4)
        board_with_started_disks = Board(4)
        board_almost_full_with_different_players = Board(4)
        board_with_one_row_empty = Board(4)
        board_with_one_column_empty = Board(4)

        # fill board_almost_full_with_o_player
        for i in range(4):
            for j in range(4):
                if i != 2 and j != 2:
                    board_almost_full_with_o_player.update_cell(i, j, Player.O)

        # fill board_almost_full_with_x_player
        for i in range(4):
            for j in range(4):
                if (i != 0 and j != 3) or (i != 3 and j != 1):
                    board_almost_full_with_x_player.update_cell(i, j, Player.X)

        # fill board_with_started_disks
        board_with_started_disks.update_cell(1, 1, Player.X)
        board_with_started_disks.update_cell(2, 2, Player.X)
        board_with_started_disks.update_cell(1, 2, Player.O)
        board_with_started_disks.update_cell(2, 1, Player.O)

        # fill board_almost_full_with_different_players
        for i in range(4):
            for j in range(4):
                if i > 3 or j <= 1:
                    board_almost_full_with_different_players.\
                        update_cell(i, j, Player.X)
                elif i == 2 and j == 3:
                    break
                else:
                    board_almost_full_with_different_players.\
                        update_cell(i, j, Player.O)

        # fill board_with_one_row_empty
        for i in range(4):
            for j in range(4):
                if i != 2:
                    board_with_one_row_empty.update_cell(i, j, Player.O)

        # fill board_with_one_column_empty
        for i in range(4):
            for j in range(4):
                if j != 0:
                    board_with_one_column_empty.update_cell(i, j, Player.X)

        self.assertFalse(board_almost_full_with_o_player.is_full())
        self.assertFalse(board_almost_full_with_x_player.is_full())
        self.assertFalse(board_empty.is_full())
        self.assertFalse(board_with_started_disks.is_full())
        self.assertFalse(board_almost_full_with_different_players.is_full())
        self.assertFalse(board_with_one_row_empty.is_full())
        self.assertFalse(board_with_one_column_empty.is_full())

    def test_get_cell(self):
        board = Board(4)
        board.update_cell(0, 0, Player.X)
        board.update_cell(3, 3, Player.O)
        board.update_cell(0, 3, Player.X)
        board.update_cell(1, 1, Player.O)

        self.assertEqual(board.get_cell(0, 0), Player.X)
        self.assertEqual(board.get_cell(3, 3), Player.O)
        self.assertEqual(board.get_cell(0, 3), Player.X)
        self.assertEqual(board.get_cell(1, 1), Player.O)
        self.assertIsNone(board.get_cell(-1, 0))
        self.assertEqual(board.get_cell(1, 2), board.EMPTY_CELL)

    def test_update_cell(self):
        board = Board(4)

        # updating board
        board.update_cell(0, 0, Player.X)
        board.update_cell(3, 3, Player.O)
        board.update_cell(0, 3, Player.X)
        board.update_cell(3, 0, Player.O)
        board.update_cell(1, 2, Player.X)
        board.update_cell(2, 1, Player.O)

        # check if update successful
        self.assertEqual(board.get_cell(0, 0), Player.X)
        self.assertEqual(board.get_cell(3, 3), Player.O)
        self.assertEqual(board.get_cell(0, 3), Player.X)
        self.assertEqual(board.get_cell(3, 0), Player.O)
        self.assertEqual(board.get_cell(1, 2), Player.X)
        self.assertEqual(board.get_cell(2, 1), Player.O)

        # None values
        self.assertIsNone(board.update_cell(-1, 0, Player.X))
        self.assertIsNone(board.update_cell(5, 1, Player.O))
        self.assertIsNone(board.update_cell(6, 4, Player.X))

    def test_init(self):
        with self.assertRaises(InvalidBoardSizeError):
            board = Board(-15)
        self.assertEqual(type(Board(1)), Board)
        self.assertEqual(type(Board(10)), Board)
        self.assertEqual(type(Board(3)), Board)
        self.assertEqual(type(Board(7)), Board)
        self.assertEqual(type(Board(10000)), Board)

    def test_num_disks(self):
        board = Board(4)
        board.update_cell(0, 0, Player.X)
        board.update_cell(3, 3, Player.O)
        board.update_cell(1, 3, Player.X)
        board.update_cell(0, 1, Player.O)

        self.assertEqual(len(board.num_disks().keys()), 3)
        self.assertEqual(board.num_disks()[Player.X], 2)
        self.assertEqual(board.num_disks()[Player.O], 2)
        self.assertEqual(board.num_disks()[board.EMPTY_CELL], 12)
