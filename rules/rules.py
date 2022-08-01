from model.game import Game
from model.board import Board


class ChangedRules(Game):
    def __init__(self, board_size) -> None:
        super().__init__(board_size)

    def is_valid_move(self, row, col) -> bool:
        """check validity of move if rooles allowed to put
        disks in every cells of the board

        Args:
            row (int): row of the board
            col (int): column of the board

        Returns:
            bool: validity of the move
        """
        if self.board.is_inside(row, col):
            return True
        else:
            return False
