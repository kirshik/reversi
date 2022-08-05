class InvalidBoardSizeError(Exception):
    def __init__(self, message="Please define board size correctly") -> None:
        super().__init__(message)
