from view.game_view import GameView
from view.console_board_view import BoardConsoleView
from model.game import Game
from model.board import Board


class GameConsoleView(GameView):
    symbols = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, game: Game, board: Board) -> None:
        super().__init__(game)
        self.board = board
        self.board_view = BoardConsoleView(game.board)

    def get_move(self):
        s = input('Enter your move (row, col):').split(',')
        # TODO catch exception
        row, col = int(s[0]-1), int(s[1]-1)
        return row, col

    def turn(self):
        print(f'Player {self.symbols[self.game.curr_player]}: It\'s your turn')

    def draw_board(self):
        self.board_view.draw_board()
        num_disks = Board.num_disks(self.board)
        if self.game.is_terminated():
            print(self.game.is_terminated())
            print(
                f'{num_disks.keys()[0]} score: {num_disks.values()[0]}, \
                {num_disks.keys()[1]} score: {num_disks.values()[1]} ')

    def display_winner(self, player):
        # TODO
        pass
