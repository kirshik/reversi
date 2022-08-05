from view.game_view import GameView
from view.console_board_view import BoardConsoleView
from model.game import Game
from model.board import Board
from datetime import datetime
from model.players import Player
from globals.symbols import SYMBOLS


class GameConsoleView(GameView):
    GAME_COUNT = 0

    def __init__(self, game: Game, board: Board) -> None:
        super().__init__(game)
        self.board = board
        self.board_view = BoardConsoleView(game.board)

    def display_ai_move(self, move):
        try:
            print(f'AI move: {move[0]+1}, {move[1]+1}')
        except:
            print(f'AI move: {move}')

    def get_move(self):
        """get move from the player

        Returns:
            row (int): row of the board
            col (int): column of the board
        """
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
        """show gamers whose turn now
        """
        print(f'\nPlayer {SYMBOLS[self.game.curr_player]}: It\'s your turn')
        print('To cancel the move enter \"pass\"')

    def draw_board(self):
        """dosplay board in console
        """
        self.board_view.draw_board()
        num_disks = Board.num_disks(self.board)
        if not self.game.is_terminated():
            print(
                f'X score: {num_disks[Player.X]}, O score: {num_disks[Player.O]} ')

    def display_winner(self):
        """display winner in console and append data in file
        """
        now = str(datetime.now())[:-7]
        print(self.game.check_winner(f'{self.GAME_COUNT}.txt', now), "WIN!!!")
        self.GAME_COUNT += 1

    def wrong_cell(self):
        """show exception message
        """
        print("Can't move in this cell, try again")

    def value_error_msg(self):
        print("Invalid move, try again")
