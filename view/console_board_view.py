from lib2to3.pygram import Symbols
from view.board_view import BoardView
from model.board import Board


class BoardConsoleView(BoardView):
    symbols = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, board: Board) -> None:
        super().__init__(board)

    def draw_board(self):
        """draw console board cell by cell
        """
        board_size = self.board.size
        header = "  |"

        for i in range(1, board_size + 1):
            header += f" {i} |"

        print(header)

        row_border = '--+' + '---+'*board_size

        for i in range(1, board_size + 1):
            board = f' {i}|'

            for j in range(board_size):
                cell = self.board.get_cell(i-1, j)
                board += f' {self.symbols[cell]} |'

            print(row_border)
            print(board)

        print(row_border)
