from view.console_game_view import GameConsoleView
from view.console_board_view import BoardConsoleView
from model.board import Board
from model.game import Game
b1 = Board(10)
b2 = BoardConsoleView(b1)
g1 = Game(10)
g1.put_started_disks()
g2 = GameConsoleView(g1, b1)
g2.draw_board()
g2.turn()


def check_check_lst_func(check_lst: function):
    lst = [0, 0, 0, 0, 0, 0, 0]  # cell 3 - False
    lst1 = [0, 1, 2, 0, 0, 0, 0]  # cell 3
    lst2 = [1, 2, 2, 0, 0, 0, 0]  # cell 3
    lst3 = [0, 0, 0, 0, 2, 1, 0]  # cell 3
    lst4 = [0, 0, 0, 0, 2, 2, 1]  # cell 3
    lst5 = [0, 0, 0, 0, 2, 2, 2, 1]  # cell 3
    lst6 = [1, 2, 2, 2, 0, 0, 0]  # cell 4
    lst7 = [2, 2, 2, 2, 0, 0, 0]  # cell 4 - False
    lst8 = [0, 0, 0, 2, 2, 2, 2]  # cell 3 - False
    print("lst ", check_lst(lst, 3))
    print("lst1 ", check_lst(lst1, 3))
    print("lst2 ", check_lst(lst2, 3))
    print("lst3 ", check_lst(lst3, 3))
    print("lst4 ", check_lst(lst4, 3))
    print("lst5 ", check_lst(lst5, 3))
    print("lst6 ", check_lst(lst6, 4))
    print("lst7 ", check_lst(lst7, 4))
    print("lst8 ", check_lst(lst8, 3))
