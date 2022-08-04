
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

    def is_inside(self, row, col) -> bool:
        if (0 <= row < self.size and 0 <= col < self.size):
            return True
        else:
            return False

    def is_full(self) -> bool:
        """is board full or board have empty cells
        """
        for row in self.mat:
            if self.EMPTY_CELL not in row:
                pass
            else:
                return False
        return True

    def num_disks(self):
        """function to define number of disks

        Returns:
            dict: dictionary with number of disks of players
        """
        disks = {}  # key = player symbol, value = disks number
        for row in self.mat:
            for i in row:
                if i in disks:
                    disks[i] += 1
                else:
                    disks[i] = 1
        return disks
