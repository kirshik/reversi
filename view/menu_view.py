from controller.game_controller import GameController
from model.game import Game
from view.console_game_view import GameConsoleView
from player_types.human import Human
from player_types.simple_ai import SimpleAI
from player_types.advanced_ai import AdvancedAI


class Menu:
    def __init__(self) -> None:
        pass

    @staticmethod
    def menu():
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

        print("=" * 35)
        print("     Welcome to Reversi game!")
        print("=" * 35)
        print("_" * 35, "\n     Menu")
        for option, message in OPTIONS_VIEW.items():
            print(option, message)
        print("_" * 35)
        view_option = 0
        while view_option not in OPTIONS_VIEW:
            try:
                view_option = int(input("\nPlease choose your mode: "))
            except ValueError:
                print("Sorry, you can choose only 1, 2 or 3 :(")
        print("_" * 35)
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
        board_size = ""
        while type(board_size) != int:
            try:
                board_size = int(
                    input("\nPlease choose board size(8, 10, 16 etc.): "))
            except:
                print("Please enter a number, not symbols or letters")
        print("_" * 35)
        game = Game(board_size)
        if player == 1:
            player = Human()
        elif player == 2:
            player = SimpleAI(game.board, game, game.board_size)
        else:
            player = AdvancedAI()
        if view_option == 1:
            view = GameConsoleView(game, game.board)
        elif view_option == 2:
            print("Sorry, only console view available for now(")
            view = GameConsoleView(game, game.board)
        elif view_option == 3:
            print("Sorry, only console view available for now(")
            view = GameConsoleView(game, game.board)
        g1 = GameController(view, game, player)
        g1.run_game()
