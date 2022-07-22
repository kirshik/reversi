from view.console_game_view import GameConsoleView
from view.console_board_view import BoardConsoleView
from model.board import Board
from model.game import Game
b1 = Board(8)
b2 = BoardConsoleView(b1)
g1 = Game(8)
g1.put_started_disks()
g2 = GameConsoleView(g1, b1)
g2.draw_board()
g2.turn()
