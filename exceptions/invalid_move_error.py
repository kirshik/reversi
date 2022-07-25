class InvalidMoveError(Exception):
    def __init__(self, message="You can't move in this cell") -> None:
        super().__init__(message)
