from model.board import Board
from model.game import Game
from model.players import Player
from globals.symbols import DIRECTIONS


class SimpleAI:
    def __init__(self, board: Board, game: Game) -> None:
        self.game = game
        self.board = board
        self.board_size = board.size

    def make_move(self):
        """check all possible moves and define move 
        which reverse maximux number of disks

        Returns:
            row (int): row of the board
            col (int): column of the board
        """
        move = {}
        for row in range(self.board_size):
            for col in range(self.board_size):
                target_cell = (row, col)
                if self.board.get_cell(row, col) == self.board.EMPTY_CELL:
                    for direction in DIRECTIONS:
                        curr_cell = target_cell
                        to_update = []
                        while self.board.is_inside(curr_cell[0] + direction[0],
                                                   curr_cell[1] + direction[1]):
                            curr_cell = (curr_cell[0] + direction[0],
                                         curr_cell[1] + direction[1])
                            if self.board.get_cell(curr_cell[0], curr_cell[1]) == Player(self.game.OTHER_PLAYER - self.game.curr_player):
                                to_update.append(curr_cell)
                            elif self.board.get_cell(curr_cell[0], curr_cell[1]) == self.game.curr_player and len(to_update) > 0:
                                move[len(to_update)] = (row, col)
                            else:
                                break
                else:
                    break
        try:
            row, col = move[max(move.keys())]
            return row, col
        except ValueError:
            return "pass"
