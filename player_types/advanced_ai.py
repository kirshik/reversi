from model.board import Board
from model.game import Game
from globals.symbols import DIRECTIONS
from globals.symbols import SYMBOLS
import copy
from model.players import Player
from view.console_board_view import BoardConsoleView


class AdvancedAI():
    def __init__(self, board: Board, game: Game) -> None:
        self.board = board
        self.game = game
        self.board_size = board.size
        self.heuristic_board()
        self.max_depth = 30
        self.min_score = 0

    def heuristic_board(self):
        heuristic_board = []
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                if i == 0 or i == (self.board_size - 1):
                    # if corner cell = 1000
                    if j == 0 or j == (self.board_size - 1):
                        row.append(1000)
                    # if near conor cell = 10
                    elif j == 1 or j == (self.board_size - 2):
                        row.append(-10)

                    # if up or down row cell == 10
                    else:
                        row.append(10)
                elif i == 1 or i == (self.board_size - 2):
                    if j == 0 or j == 1 or j == (self.board_size - 1) or j == (self.board_size - 2):
                        row.append(-10)
                    else:
                        row.append(10)
                else:
                    if j == 0 or j == (self.board_size - 1):
                        row.append(10)
                    else:
                        row.append(1)
            heuristic_board.append(row)
        self.heuristic_board = heuristic_board

    def heuristic_func(self, board_state: Board):
        res = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board_state.get_cell(i, j) == Player.O:
                    res += self.heuristic_board[i][j]
                elif board_state.get_cell(i, j) == Player.X:
                    res -= self.heuristic_board[i][j]
        return res

    def minimax(self, board: Board, max_player, min_player, depth):
        score = self.heuristic_func(board)
        if depth > self.max_depth:
            return score
        if score < self.min_score:
            return score

        game = Game(board)
        if max_player % 2:
            game.change_player()
        # if game in terminal state return 1/-1/0 for win/lose/draw for  AI
        if game.is_terminated():
            if game.check_winner() == SYMBOLS[max_player]:
                return 10**5
            elif game.check_winner() == SYMBOLS[min_player]:
                return -10**5
            else:
                return 0

        values = []
        possible_moves = []
        # possible_moves for AI player
        for i in range(self.board_size):
            for j in range(self.board_size):
                if game.is_valid_move(i, j):
                    possible_moves.append((i, j))
        for move in possible_moves:
            new_board = copy.deepcopy(board)
            new_game = Game(new_board)
            if max_player % 2:
                new_game.change_player()
            new_game.make_move(move[0], move[1])

            board_value = self.minimax(
                new_board, min_player, max_player, depth+1)

            values.append(board_value)

        if Player.X == max_player:
            return max(values)
        else:
            return min(values)

    def choose_move(self):
        possible_moves = []
        # possible_moves for AI player
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.game.is_valid_move(i, j):
                    possible_moves.append((i, j))

        board_values = {}
        for move in possible_moves:
            new_board = copy.deepcopy(self.board)
            new_game = Game(new_board)
            new_game.change_player()
            new_game.make_move(move[0], move[1])
            board_value = self.minimax(
                new_board, self.game.curr_player, Player(self.game.OTHER_PLAYER - self.game.curr_player), depth=1)
            board_values[move] = board_value
        return max(board_values, key=board_values.get)

    def make_move(self):
        return self.choose_move()
