from re import I
import unittest

from rules.rules import ChangedRules
from model.board import Board
from model.game import Game


class TestBoard(unittest.TestCase):

    def test_changed_is_valid_positives_cases(self):
        board = Board(4)
        game = ChangedRules(board)
        game.put_started_disks()

        # test corners
        self.assertTrue(game.is_valid_move(0, 0))
        self.assertTrue(game.is_valid_move(3, 3))
        self.assertTrue(game.is_valid_move(0, 3))
        self.assertTrue(game.is_valid_move(3, 0))

        # test empty cells
        self.assertTrue(game.is_valid_move(2, 0))
        self.assertTrue(game.is_valid_move(2, 3))

    def test_changed_is_valid_negatives_cases(self):
        board = Board(4)
        game = ChangedRules(board)
        game.put_started_disks()

        # test occupied cells
        self.assertFalse(game.is_valid_move(1, 2))
        self.assertFalse(game.is_valid_move(2, 1))
        self.assertFalse(game.is_valid_move(1, 1))

        # test cells outside the board
        self.assertFalse(game.is_valid_move(-1, 5))
        self.assertFalse(game.is_valid_move(2, 7))
        self.assertFalse(game.is_valid_move(-1, -10))
