
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

    # TODO check if i use it somewhere or not
    def get_matrix(self) -> list:  # board matrix
        return self.mat

    def get_row(self, row) -> list:
        return self.mat[row]

    def get_column(self, col) -> list:
        column = []
        for i in range(self.size):
            column.append(self.mat[i][col])
        return column

    def get_diagonal(self, row, col) -> list:
        diag_up = []
        diag_down = []
        row_copy = row
        col_copy = col
        cell = [self.mat[row][col]]
        while (len(diag_up)+len(diag_down)+1) != self.size:
            if (row_copy - 1) >= 0 and (col_copy + 1) <= (self.size - 1):
                diag_up.append(self.mat[row_copy - 1][col_copy + 1])
                row_copy -= 1
                col_copy += 1
            elif (row + 1) <= (self.size - 1) and (col - 1) >= 0:
                diag_down.append(self.mat[row + 1][col - 1])
                row += 1
                col -= 1
            else:
                break
        # return list with diagonal and place of cell user want to change
        return [(diag_down + cell + diag_up), len(diag_down)]

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
