from view.game_view import GameView
from view.console_board_view import BoardConsoleView
from model.game import Game


class GameConsoleView(GameView):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.board_view = BoardConsoleView(game.board)

    def get_move(self):
        s = input('Enter your move (row, col):').split(',')
        # TODO catch exception
        row, col = int(s[0]-1), int(s[1]-1)
        return row, col

    def draw_board(self):
        self.board_view.draw_board()

    def turn(self):
        print(f'Player {self.game.curr_player}: It\'s your turn')
        # TODO
        pass

    def display_winner(self, player):
        # TODO
        pass
