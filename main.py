from controller.game_controller import GameController
from model.game import Game


def menu():
    print("=" * 35)
    print("     Welcome to Reversi game!")
    print("=" * 35)
    print("_" * 35, "\n     Menu")
    print("1 - for playing Reversi in console")
    print("2 - for playing Reversi in web")
    print("3 - for playing Reversi in graphic view")
    print("_" * 35)
    try:
        view = int(input("Please choose your mode: "))
    except ValueError:
        print("Sorry, you can choose only 1, 2 or 3 :(")
    print("_" * 35)
    try:
        board_size = int(input("Please choose board size(8, 10, 16 etc.): "))
    except:
        print("Please enter a number, not symbols or letters")
    print("_" * 35)
    game = Game(board_size)
    g1 = GameController(view, game)
    g1.run_game()


menu()
