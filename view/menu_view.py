from controller.game_controller import GameController
from model.game import Game
from view.console_game_view import GameConsoleView
from player_types.human import Human
from player_types.simple_ai import SimpleAI
from player_types.advanced_ai import AdvancedAI
from model.board import Board
from rules.rules import ChangedRules
from view.graphic_menu_view import Reversi, GEOMETRY


class Menu:
    def __init__(self) -> None:
        pass

    @staticmethod
    def menu():
        """display menu
        """
        OPTIONS_VIEW = {
            1: "- for playing Reversi in console",
            2: "- for playing Reversi in web",
            3: "- for playing Reversi in graphic view"
        }
        OPTIONS_PLAYER = {
            1: "- for playing agains human",
            2: "- for playing agains simple AI",
            3: "- for playing agains advanced AI"
        }
        OPTIONS_RULES = {
            1: "- for playing with \"open\", where you can put disks anywere",
            2: "- for playing with standart Reversi rools"
        }

        print("=" * 35)
        print("     Welcome to Reversi game!")
        print("=" * 35)
        print("_" * 35, "\n     Menu")

        # get view type from user
        for option, message in OPTIONS_VIEW.items():
            print(option, message)
        print("_" * 35)
        view_option = 0
        while view_option not in OPTIONS_VIEW:
            try:
                view_option = int(input("\nPlease choose your mode: "))
            except ValueError:
                print("Sorry, you can choose only 1 or 3 :(")
        print("_" * 35)
        if view_option == 3:
            app = Reversi()
            app.geometry(GEOMETRY)
            app.mainloop()

        # get rules type from user
        for option, message in OPTIONS_RULES.items():
            print(option, message)
        print("_" * 35)
        rule_option = 0
        while rule_option not in OPTIONS_VIEW:
            try:
                rule_option = int(input("\nPlease choose rools: "))
            except ValueError:
                print("Sorry, you can choose only 1 or 2 :(")
        print("_" * 35)

        # get player type from user
        player = ""
        for option, player in OPTIONS_PLAYER.items():
            print(option, player)
        print("_" * 35)
        while player not in OPTIONS_PLAYER:
            try:
                player = int(input("\nPlease choose your enemy: "))
            except ValueError:
                print("Sorry, you can choose only 1, 2 or 3 :(")
        print("_" * 35)

        # get board size from user
        board_size = ""
        while type(board_size) != int:
            try:
                board_size = int(
                    input("\nPlease choose board size(8, 10, 16 etc.): "))
            except:
                print("Please enter a number, not symbols or letters")
        print("_" * 35)

        board = Board(board_size)
        # rule type
        if rule_option == 1:
            game = ChangedRules(board)
        else:
            game = Game(board)
        # player type
        if player == 1:
            player = Human()
        elif player == 2:
            player = SimpleAI(board, game)
        else:
            player = AdvancedAI(board, game)
        # view type
        if view_option == 1:
            view = GameConsoleView(game, game.board)
        elif view_option == 2:
            print("Sorry, only console view available for now(")
            view = GameConsoleView(game, game.board)

        g1 = GameController(view, game, player)
        g1.run_game()
