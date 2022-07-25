from model.game import Game
from rules.rules import ChangedRules
from view.console_board_view import BoardConsoleView
from view.console_game_view import GameConsoleView
from exceptions.invalid_move_error import InvalidMoveError


class GameController:
    def __init__(self, view, game: Game) -> None:
        self.view = view
        self.game = game

    def choose_rule(self):
        print()

    def run_game(self):
        self.game.put_started_disks()
        console_game = GameConsoleView(self.game, self.game.board)
        console_game.draw_board()
        console_game.turn()
        while not self.game.is_terminated():
            row, col = console_game.get_move()
            if self.game.is_valid_move(row, col):
                self.game.make_move(row, col)
                console_game.draw_board()
                self.game.change_player()
                console_game.turn()
                print("\n")
            else:
                raise InvalidMoveError
