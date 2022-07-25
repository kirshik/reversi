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
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        target_cell = (row, col)
        for direction in directions:
            curr_cell = target_cell
            to_update = []
            while self.board.is_inside(curr_cell[0], curr_cell[1]):
                curr_cell = (curr_cell[0] + direction[0],
                             curr_cell[1] + direction[1])
                if self.board.get_cell(curr_cell[0], curr_cell[1]) == self.OTHER_PLAYER - self.curr_player:
                    to_update.append(curr_cell)
                elif self.board.get_cell(curr_cell[0], curr_cell[1]) == self.curr_player and len(to_update) > 0:
                    return True
                else:
                    break
        return False

    def make_move(self, row, col):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        target_cell = (row, col)
        for direction in directions:
            curr_cell = target_cell
            to_update = []
            while self.board.is_inside(curr_cell[0], curr_cell[1]):
                curr_cell = (curr_cell[0] + direction[0],
                             curr_cell[1] + direction[1])
                if self.board.get_cell(curr_cell[0], curr_cell[1]) == self.OTHER_PLAYER - self.curr_player:
                    to_update.append(curr_cell)
                elif self.board.get_cell(curr_cell[0], curr_cell[1]) == self.curr_player and len(to_update) > 0:
                    for i in to_update:
                        self.board.update_cell(i[0], i[1], self.curr_player)
                else:
                    break
        self.board.update_cell(row, col, self.curr_player)

    def is_terminated(self) -> boolean:
        if self.board.is_full() or len(self.board.num_disks().keys()) == 1:
            return True
        else:
            return False

    def check_winner(self, path, date_time):
        # dictionary key = player symbol, value = disks number
        num_disks = self.board.num_disks()
        max_val = max(num_disks.values())
        winner = [key[0] for key in num_disks.items() if key[1] == max_val][0]
        summary = (f'Date and time of the Game: {date_time}\n \
                     {Player(winner)}\n\
                         X: {num_disks[Player.X]} , O: {num_disks[Player.O]}')

        if self.is_terminated():
            with open(path) as f:
                f.write(summary)
            return summary