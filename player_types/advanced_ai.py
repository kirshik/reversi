from model.board import Board
from model.game import Game
from globals.symbols import DIRECTIONS
from globals.symbols import SYMBOLS
import copy


class AdvancedAI():
    def __init__(self, board: Board, game: Game, board_size: int) -> None:
        self.board = board
        self.game = game
        self.board_size = board_size

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

        return heuristic_board

    def make_possible_move(self, board: Board, row, col):
        """make possible move inside the choose move function

        Args:
            row (int): row of board
            col (int): column of board
        """
        target_cell = (row, col)
        for direction in DIRECTIONS:
            curr_cell = target_cell
            to_update = []
            while board.is_inside(curr_cell[0] + direction[0],
                                  curr_cell[1] + direction[1]):
                curr_cell = (curr_cell[0] + direction[0],
                             curr_cell[1] + direction[1])
                if board.get_cell(curr_cell[0], curr_cell[1]) == self.game.OTHER_PLAYER - self.game.curr_player:
                    to_update.append(curr_cell)
                elif board.get_cell(curr_cell[0], curr_cell[1]) == self.game.curr_player and len(to_update) > 0:
                    for i in to_update:
                        board.update_cell(i[0], i[1], self.game.curr_player)
                else:
                    break
        board.update_cell(row, col, self.game.curr_player)

    def minimax(self, board: Board, max_player, min_player):
        game = Game(self.board_size, board)
        # change player to O, becouse O - AI player as defolt
        game.change_player()
        # if game in terminal state return 1/-1/0 for win/lose/draw for  AI
        if game.is_terminated():
            if game.check_winner("advancedAI.txt", "date") == SYMBOLS[max_player]:
                return 1
            elif game.check_winner("advancedAI.txt", "date") == SYMBOLS[min_player]:
                return -1
            else:
                return 0
        values = []
        possible_moves = []
        # possible_moves for AI player
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board.get_cell(i, j) == self.board.EMPTY_CELL:
                    if game.is_valid_move(i, j):
                        possible_moves.append((i, j))
        for move in possible_moves:
            new_board = copy.deepcopy(board)

            #self.make_possible_move(new_board, move[0], move[1])

            game.make_move(move[0], move[1])
            board_value = self.minimax(new_board, min_player, max_player)
            values.append(board_value)
        if game.curr_player == max_player:
            return max(values)
        else:
            return min(values)

    def choose_move(self):
        possible_moves = []
        # possible_moves for AI player
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board.get_cell(i, j) == self.board.EMPTY_CELL:
                    if self.game.is_valid_move(i, j):
                        possible_moves.append((i, j))
        # change_player
        self.game.change_player()
        possible_moves_other_player = []
        # possible moves for other player
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board.get_cell(i, j) == self.board.EMPTY_CELL:
                    if self.game.is_valid_move(i, j):
                        possible_moves_other_player.append((i, j))
        # change player back to save the game logic
        self.game.change_player()
        board_values = {}
        for move in possible_moves:
            new_board = copy.deepcopy(self.board)
            self.make_possible_move(new_board, move[0], move[1])
            board_value = self.minimax(
                new_board, self.game.curr_player, self.game.OTHER_PLAYER - self.game.curr_player)
            board_values[board_value] = move
        self.game.change_player()

        for move in possible_moves_other_player:
            new_board = copy.deepcopy(self.board)
            self.make_possible_move(new_board, move[0], move[1])
            board_value = self.minimax(
                new_board, self.game.OTHER_PLAYER - self.game.curr_player, self.game.curr_player)
            board_values[board_value] = move
        self.game.change_player()

        return board_values[max(board_values)]

    def make_move(self):
        self.choose_move()
