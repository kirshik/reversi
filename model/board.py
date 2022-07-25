
class Board:
    """define board, board size
    """
    EMPTY_CELL = 0

    def __init__(self, size) -> None:
        self.size = size
        # Allocate the board with empty squares
        self.mat = [[self.EMPTY_CELL] * size for _ in range(size)]

    def get_cell(self, row, column):
        return self.mat[row][column]

    def update_cell(self, row, column, player):
        self.mat[row][column] = player

    def is_inside(self, row, col):
        if (0 <= row, col < self.size):
            return True
        else:
            return False

    def is_full(self):
        for row in self.mat:
            if self.EMPTY_CELL not in row:
                pass
            else:
                return False
        return True

    def num_disks(self):
        disks = {}  # key = player symbol, value = disks number
        for row in self.mat:
            for i in row:
                if i in disks:
                    disks[i] += 1
                else:
                    disks[i] = 1
        return disks
