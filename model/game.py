from xmlrpc.client import boolean
from model.board import Board
from model.players import Player


class Game:
    OTHER_PLAYER = 3

    def __init__(self, board_size) -> None:
        self.board_size = board_size
        self.board = Board(board_size)
        self.curr_player = Player.X

    def put_started_disks(self):
        absolut_pos = self.board_size//2 - 1
        other_player = self.OTHER_PLAYER - self.curr_player
        # 1 disk current player
        self.board.update_cell(
            absolut_pos, absolut_pos, self.curr_player)
        # 2 disk current player
        self.board.update_cell(
            absolut_pos + 1, absolut_pos + 1, self.curr_player)
        # 3 disk other player
        self.board.update_cell(absolut_pos, absolut_pos + 1, other_player)
        # 4 disk other player
        self.board.update_cell(absolut_pos + 1, absolut_pos, other_player)

    def change_player(self):
        self.curr_player = self.OTHER_PLAYER - self.curr_player

    def is_valid_move(self, row, col) -> bool:
        """dinamical function depends of the rools
        show valid of player move

        Args:
            row (int): row of board
            col (int): column of board
        """

        def check_lst(lst, cell):
            other_player = self.OTHER_PLAYER - self.curr_player

            i = cell + 1
            check_i = set()
            while i < len(lst):
                if lst[i] == other_player or other_player in check_i:
                    check_i.add(other_player)
                    if (i + 1) < len(lst) and lst[i + 1] == self.curr_player:
                        return True
                i += 1

            j = cell - 1
            check_j = set()
            while j > 0 and j < len(lst[:j + 1]):
                if lst[j] == other_player or other_player in check_j:
                    check_j.add(other_player)
                    if (j - 1) >= 0 and lst[j - 1] == self.curr_player:
                        return True
                j -= 1

            return False

        if self.board.get_row(row)[col] != self.board.EMPTY_CELL:
            return False
        else:
            check_row = check_lst(self.board.get_row(row),
                                  self.board.get_row(row)[col])

            check_col = check_lst(self.board.get_column(col),
                                  self.board.get_column(col)[row])

            check_diag = check_lst(self.board.get_diagonal(row, col)[0],
                                   self.board.get_diagonal(row, col)[1])

            if check_row and check_col and check_diag:
                return True
            else:
                return False
#
#
#
#
#

    def make_move(self, row, col):
        # TODO
        def update_right(lst, cell):
            other_player = self.OTHER_PLAYER - self.curr_player
            i = cell + 1
            check_i = set()
            while i < len(lst):
                if lst[i] == other_player or other_player in check_i:
                    check_i.add(other_player)
                    if (i + 1) < len(lst) and lst[i + 1] == self.curr_player:
                        return True
                i += 1

        def update_left(lst, cell):
            other_player = self.OTHER_PLAYER - self.curr_player
            j = cell - 1
            check_j = set()
            while j > 0 and j < len(lst[:j + 1]):
                if lst[j] == other_player or other_player in check_j:
                    check_j.add(other_player)
                    if (j - 1) >= 0 and lst[j - 1] == self.curr_player:
                        return True
                j -= 1

        def update_cell_of_row(lst, cell):
            pass

        def update_cell_of_col(lst, cell):
            pass

        def update_cell_of_diag(lst, cell):
            pass
        update_cell_of_row(self.board.get_row(row),
                           self.board.get_row(row)[col])
        update_cell_of_col(self.board.get_column(col),
                           self.board.get_column(col)[row])
        update_cell_of_diag(self.board.get_diagonal(row, col)[0],
                            self.board.get_diagonal(row, col)[1])

#
#
#
#
#
#
#

    def is_terminated(self) -> boolean:
        if self.board.is_full() or len(self.board.num_disks().keys()) == 1:
            return True
        else:
            return False

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
