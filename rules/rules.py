from model.game import Game
from model.board import Board


class ChangedRules(Game):
    def __init__(self, board_size) -> None:
        super().__init__(board_size)

    def is_valid_move(self, row, col) -> bool:
        if self.board.is_inside(row, col):
            return True
        else:
            return False
