from model.board import Board
from model.game import Game
from globals.symbols import DIRECTIONS


class SimpleAI:
    def __init__(self, board: Board, game: Game, board_size: int) -> None:
        self.game = game
        self.board = board
        self.board_size = board_size

    def make_move(self):
        move = {}
        for row in range(self.board_size):
            for col in range(self.board_size):
                target_cell = (row, col)
                for direction in DIRECTIONS:
                    curr_cell = target_cell
                    to_update = []
                    while self.board.is_inside(curr_cell[0] + direction[0],
                                               curr_cell[1] + direction[1]):
                        curr_cell = (curr_cell[0] + direction[0],
                                     curr_cell[1] + direction[1])
                        if self.board.get_cell(curr_cell[0], curr_cell[1]) == self.game.OTHER_PLAYER - self.game.curr_player:
                            to_update.append(curr_cell)
                        elif self.board.get_cell(curr_cell[0], curr_cell[1]) == self.game.curr_player and len(to_update) > 0:
                            move[len(to_update)] = (row, col)
                        else:
                            break
        row, col = move[max(move.keys())]
        return row, col
