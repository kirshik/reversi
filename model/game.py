from model.board import Board
from model.players import Player


class Game:
    OTHER_PLAYER = 3

    def __init__(self, board_size) -> None:
        self.board_size = board_size
        self.board = Board(board_size)
        self.curr_player = Player.X

    def change_player(self):
        self.curr_player = self.OTHER_PLAYER - self.curr_player

    def make_move(self, row, col):
        # TODO write func and all condotions, update a lot of cells
        board_mat = self.board.get_matrix()
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.board.update_cell(row, col, self.curr_player)

    def is_disks_couse_flip(self, row, col):
        # TODO
        pass

    def is_valid_move(self, row, col):
        """dinamical function depends of the rools
        show valid of player move

        Args:
            row (int): row of board
            col (int): column of board
        """
        # TODO
        pass

    def check_winner(self):
        # dictionary key = player symbol, value = disks number
        num_disks = self.board.num_disks()

        if self.board.is_full():

            if num_disks[self.curr_player] > \
                    num_disks[self.OTHER_PLAYER - self.curr_player]:
                return self.curr_player

            else:
                return self.OTHER_PLAYER - self.curr_player

        elif len(num_disks.keys()) == 1:
            return num_disks.items()[0]
