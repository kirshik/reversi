from model.game import Game
from rules.rules import ChangedRules
from view.game_view import GameView
from globals.symbols import PLAYERS
from player_types.human import Human
from player_types.simple_ai import SimpleAI
from player_types.advanced_ai import AdvancedAI
from model.players import Player


class GameController:
    def __init__(self, view: GameView, game: Game, player_type) -> None:
        self.player_type = player_type
        self.view = view
        self.game = game

    def choose_rule(self):
        # TODO
        print()

    def run_game(self):
        """put started disks, identificate
         player and run the game
        """
        self.game.put_started_disks()
        console_game = self.view
        console_game.draw_board()
        console_game.turn()
        while not self.game.is_terminated():
            try:
                if type(self.player_type) == Human:
                    get_move = console_game.get_move()
                elif type(self.player_type) == SimpleAI:
                    if self.game.curr_player == Player.O:
                        get_move = self.player_type.make_move()
                    else:
                        get_move = console_game.get_move()
                else:
                    if self.game.curr_player == Player.O:
                        get_move = self.player_type.make_move()
                    else:
                        get_move = console_game.get_move()
                if get_move != "pass":
                    row, col = get_move
                    if self.game.is_valid_move(row, col):
                        self.game.make_move(row, col)
                        console_game.draw_board()
                        self.game.change_player()
                        console_game.turn()
                    else:
                        console_game.wrong_cell()
                else:
                    if not self.game.is_terminated():
                        self.game.change_player()
                        console_game.turn()
            except ValueError:
                console_game.value_error_msg()
        console_game.display_winner()
