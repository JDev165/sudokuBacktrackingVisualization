import pygame
from constants import *
from pygame.locals import *


class Cartridge:
    def __init__(self, title):
        self.title = title

    def play(self):
        pass

    def _setUp(self):
        pass


class Sudoku(Cartridge):
    def __init__(self, title, boardSize):
        self.title = title
        self.boardSize = boardSize
        self.sudoku_board = Rect(self.boardSize, self.boardSize)
        self.buttons = []
        self.wrongChoices = {}
        self.centered_board_zero_x_cord = 0
        self.centered_board_width_cord = 0
        self.centered_board_height_cord = 0
        self.selection_pos = None
        self.sudoku_array_coords = None
        self.selection_rect = None
        self.clicked_inside_board = None
        self.valid_selection = None

    def getBoard(self):
        return self.sudoku_board

    def play(self, screen):
        updated_screen = self._setUp(screen)
        return updated_screen

    def _setUp(self, screen):
        self.sudoku_board.centery = CENTER_SCREEN_X
        self.sudoku_board.centerx = CENTER_SCREEN_Y

        # Board is shifted after we center it so we have to get the new coordinates to
        # Draw the board lines
        # centered_board_zero_x_cord = 54
        self.centered_board_zero_x_cord = self.sudoku_board.topleft[0]
        self.centered_board_width_cord = self.sudoku_board.topright[0]
        self.centered_board_height_cord = self.sudoku_board.bottomleft[1]

        # 540 width/height, 54 origin of centered sudoku board
        # 540/3 = 180 + 54 (origin) = 234
        # Second vertical line starting point = 234 = 180+180+54
        startBigSquares = self.centered_board_zero_x_cord + SUDOKU_BOARD_LARGE_SQUARE_SIZE
        stopBigSquares = self.centered_board_zero_x_cord + \
            (SUDOKU_BOARD_LARGE_SQUARE_SIZE * 3)
        startY = self.centered_board_width_cord + SUDOKU_BOARD_LARGE_SQUARE_SIZE
        stopY = self.centered_board_width_cord + \
            (SUDOKU_BOARD_LARGE_SQUARE_SIZE * 3)
        incrementBigSquares = SUDOKU_BOARD_LARGE_SQUARE_SIZE
        thickness = 4
        startSmallSquares = self.centered_board_width_cord + SUDOKU_BOARD_SMALL_SQUARE_SIZE
        stopSmallSquares = self.centered_board_width_cord + \
            (SUDOKU_BOARD_SMALL_SQUARE_SIZE * 9)
        incrementSmallSquares = SUDOKU_BOARD_SMALL_SQUARE_SIZE

        screen = self._drawSudokuBoard(startBigSquares, startSmallSquares, stopBigSquares,
                                       stopSmallSquares, incrementBigSquares, incrementSmallSquares, thickness, screen)
        return screen

    def _drawSudokuBoard(self, startBigSquares, startSmallSquares, stopBigSquares, stopSmallSquares, incrementBigSquares, incrementSmallSquares, thickness, screen):
        # After screen fill so grid won't get overwritten
        for xcord in range(startBigSquares, stopBigSquares, incrementBigSquares):
            pygame.draw.line(screen, BLACK, (xcord, self.centered_board_zero_x_cord),
                             (xcord, self.centered_board_width_cord), thickness)
            ycord = xcord
            pygame.draw.line(screen, BLACK, (self.centered_board_zero_x_cord, ycord),
                             (self.centered_board_width_cord, ycord), thickness)

        for xcord in range(startSmallSquares, stopSmallSquares, incrementSmallSquares):
            pygame.draw.line(screen, BLACK, (xcord, self.centered_board_zero_x_cord),
                             (xcord, self.centered_board_width_cord))
            ycord = xcord
            pygame.draw.line(screen, BLACK, (self.centered_board_zero_x_cord,
                                             ycord), (self.centered_board_width_cord, ycord))
        return screen
