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
        self.buttons = []
        self.wrongChoices = {}
        self.centered_board_zero_x_cord = 0
        self.centered_board_width_cord = 0
        self.centered_board_height_cord = 0

    def play(self):
        pass

    def _setUp(self):
        sudoku_board = Rect(self.boardSize, self.boardSize)
        sudoku_board.centery = CENTER_SCREEN_X
        sudoku_board.centerx = CENTER_SCREEN_Y

        # Board is shifted after we center it so we have to get the new coordinates to
        # Draw the board lines
        # centered_board_zero_x_cord = 54
        self.centered_board_zero_x_cord = sudoku_board.topleft[0]
        self.centered_board_width_cord = sudoku_board.topright[0]
        self.centered_board_height_cord = sudoku_board.bottomleft[1]

        # 540 width/height, 54 origin of centered sudoku board
        # 540/3 = 180 + 54 (origin) = 234
        # Second vertical line starting point = 234 = 180+180+54
        startSquares = self.centered_board_zero_x_cord + SUDOKU_BOARD_LARGE_SQUARE_SIZE
        stopSquares = self.centered_board_zero_x_cord + \
            (SUDOKU_BOARD_LARGE_SQUARE_SIZE * 3)
