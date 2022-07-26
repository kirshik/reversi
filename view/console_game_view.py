from view.game_view import GameView
from view.console_board_view import BoardConsoleView
from model.game import Game
from model.board import Board
from datetime import datetime


class GameConsoleView(GameView):
    GAME_COUNT = 0
    symbols = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, game: Game, board: Board) -> None:
        super().__init__(game)
        self.board = board
        self.board_view = BoardConsoleView(game.board)

    def get_move(self):
        s = input('Enter your move (row, col):').split(',')
        if s[0] != "pass":
            if len(s) > 1:
                row, col = int(s[0]) - 1, int(s[1]) - 1
                return row, col
            else:
                return -1, -1
        else:
            return "pass"

    def turn(self):
        print(
            f'\nPlayer {self.symbols[self.game.curr_player]}: It\'s your turn')
        print('To cancel the move enter \"pass\"')

    def draw_board(self):
        self.board_view.draw_board()
        num_disks = Board.num_disks(self.board)
        if not self.game.is_terminated():
            print(
                f'X score: {list(num_disks.values())[1]}, O score: {list(num_disks.values())[2]} ')

    def display_winner(self):
        now = str(datetime.now())[:-7]
        print(self.game.check_winner(f'{self.GAME_COUNT}.txt', now), "WIN!!!")
        self.GAME_COUNT += 1

    def wrong_cell(self):
        print("Can't move in this cell, try again")

    def value_error_msg(self):
        print("Invalid move, try again")
