class cartridge:
    def __init__(self, title):
        self.title = title

    def play(self):
        pass

    def _setUp(self):
        pass


class sudoku(cartridge):
    def __init__(self, title, boardSize):
        self.title = title
        self.boardSize = boardSize
        self.sudoku_board = None

    def play(self):
        pass

    def _setUp(self):
        sudoku_board = Rect(self.boardSize, self.boardSize)
        sudoku_board.centery = CENTER_SCREEN_X
        sudoku_board.centerx = CENTER_SCREEN_Y
