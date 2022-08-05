import unittest

from player_types.advanced_ai import AdvancedAI
from model.board import Board
from model.game import Game


class TestAdvancedAI(unittest.TestCase):
    def test_heroutic_board(self):
        board = Board(8)
        game = Game(board)
        ai = AdvancedAI(board, game)
        self.assertEqual(len(ai.heuristic_board()), 8)
