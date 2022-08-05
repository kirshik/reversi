import unittest

from pyrsistent import b

from model.board import Board
from model.game import Game
from player_types.simple_ai import SimpleAI
from model.players import Player


class TestSimpleAi(unittest.TestCase):
    def test_make_move(self):
        board = Board(4)
        game = Game(board)
        game.put_started_disks()

        ai = SimpleAI(board, game)
        row, col = ai.make_move()
        game.make_move(row, col)

        # test max for 1 move
        self.assertEqual(board.num_disks()[Player.X], 4)

        # test max for first O player move
        game.change_player()
        row, col = ai.make_move()
        game.make_move(row, col)
        self.assertEqual(board.num_disks()[Player.O], 3)

        # test max for 2 move
        game.change_player()
        row, col = ai.make_move()
        game.make_move(row, col)
        self.assertEqual(board.num_disks()[Player.X], 5)

        # test for ability to pass
        game.change_player()
        for i in range(4):
            for j in range(4):
                if (i == 3 and j == 0) or (i == 1 and j == 3) or (i == 2 and j == 3) or (i == 3 and j == 3):
                    board.update_cell(i, j, board.EMPTY_CELL)
                elif i == 0 and j == 3:
                    board.update_cell(i, j, Player.X)
                else:
                    board.update_cell(i, j, Player.O)
        result = ai.make_move()
        self.assertEqual(result, "pass")
