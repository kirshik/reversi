from xmlrpc.client import boolean
from model.board import Board
from model.players import Player
from globals.symbols import SYMBOLS, DIRECTIONS

class Game:
    OTHER_PLAYER = 3

    def __init__(self, board: Board) -> None:
        self.board_size = board.size
        self.board = board
        self.curr_player = Player.X

    def put_started_disks(self):
        """put 4 started disks in the midle of board
        """
        absolut_pos = self.board_size//2 - 1
        other_player = Player(self.OTHER_PLAYER - self.curr_player)
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
        self.curr_player = Player(self.OTHER_PLAYER - self.curr_player)

    def is_valid_move(self, row: int, col: int) -> bool:
        """dinamical function depends of the rools
        show valid of player move
        go by all directions and check validity of move

        Args:
            row (int): row of board
            col (int): column of board
        """
        target_cell = (row, col)
        if self.board.get_cell(row, col) == self.board.EMPTY_CELL:

            # Go over all directrions and check cells with other player disks
            # then turn them over
            for direction in DIRECTIONS:
                curr_cell = target_cell
                to_update = []
                while self.board.is_inside(curr_cell[0] + direction[0],
                                           curr_cell[1] + direction[1]):
                    curr_cell = (curr_cell[0] + direction[0],
                                 curr_cell[1] + direction[1])
                    if self.board.get_cell(curr_cell[0], curr_cell[1]) == Player(self.OTHER_PLAYER - self.curr_player):
                        to_update.append(curr_cell)
                    elif self.board.get_cell(curr_cell[0], curr_cell[1]) == self.curr_player and len(to_update) > 0:
                        return True
                    else:
                        break
        else:
            return False
        return False

    def make_move(self, row: int, col: int):
        """make move by updating cells in all directions

        Args:
            row (int): row of board
            col (int): column of board
        """
        if self.is_valid_move(row, col):
            target_cell = (row, col)
            for direction in DIRECTIONS:
                curr_cell = target_cell
                to_update = []
                while self.board.is_inside(curr_cell[0] + direction[0],
                                           curr_cell[1] + direction[1]):
                    curr_cell = (curr_cell[0] + direction[0],
                                 curr_cell[1] + direction[1])
                    if self.board.get_cell(curr_cell[0], curr_cell[1]) == self.OTHER_PLAYER - self.curr_player:
                        to_update.append(curr_cell)
                    elif self.board.get_cell(curr_cell[0], curr_cell[1]) == self.curr_player and len(to_update) > 0:
                        for i in to_update:
                            self.board.update_cell(
                                i[0], i[1], self.curr_player)
                    else:
                        break
            self.board.update_cell(row, col, self.curr_player)
        else:
            return None

    def is_terminated(self) -> bool:
        """check game termination
        """
        valid_moves = 0
        # check for valid moves for curr player
        # by check all cells
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board.get_cell(i, j) == self.board.EMPTY_CELL:
                    if self.is_valid_move(i, j):
                        valid_moves += 1
                        return False
                else:
                    pass
        # change player and check his valid moves
        self.change_player()
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board.get_cell(i, j) == self.board.EMPTY_CELL:
                    if self.is_valid_move(i, j):
                        valid_moves += 1
                        return False
                else:
                    pass
        # change player back to save curr player position
        self.change_player()

        if self.board.is_full() or len(self.board.num_disks().keys()) == 2 or valid_moves == 0:
            return True
        else:
            return False

    def check_winner(self, path=None, date_time=None):
        """define winner and write data of the game in file

        Args:
            path (str): path where file must be
            date_time (str): date and time of the game

        Returns:
            int: winners symbol
        """
        # dictionary key = player symbol, value = disks number
        num_disks = self.board.num_disks()
        if Player.X not in num_disks:
            num_disks[Player.X] = 0
        if Player.O not in num_disks:
            num_disks[Player.O] = 0
        if num_disks[Player.X] > num_disks[Player.O]:
            winner = Player.X
        elif num_disks[Player.O] > num_disks[Player.X]:
            winner = Player.O
        else:
            winner = 0
        summary = (
            f'Date and time of the Game: {date_time}\n Winner: {SYMBOLS[winner]}\n X: {num_disks[Player.X]} , O: {num_disks[Player.O]}')
        
        if self.is_terminated():
            if not path is None:
                with open(path, "w") as f:
                    f.write(summary)
            return SYMBOLS[winner]
