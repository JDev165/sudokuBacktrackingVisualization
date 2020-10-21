import pygame
from constants import *
from button import *
from pygame.locals import *
from sudoku_api import *
from sudoku import *


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
        self.font = None
        self.wrongChoices = {}
        self.centered_board_zero_x_cord = 0
        self.centered_board_width_cord = 0
        self.centered_board_height_cord = 0
        self.selection_pos = None
        self.sudoku_array_coords = None
        self.selection_rect = None
        self.clicked_inside_board = None
        self.valid_selection = None
        self.is_editable_cell = None
        self.sudoku_board.centery = CENTER_SCREEN_X
        self.sudoku_board.centerx = CENTER_SCREEN_Y
        self.board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
                      [6, 8, 0, 0, 7, 0, 0, 9, 0],
                      [1, 9, 0, 0, 0, 4, 5, 0, 0],
                      [8, 2, 0, 1, 0, 0, 0, 4, 0],
                      [0, 0, 4, 6, 0, 2, 9, 0, 0],
                      [0, 5, 0, 0, 0, 3, 0, 2, 8],
                      [0, 0, 9, 3, 0, 0, 0, 7, 4],
                      [0, 4, 0, 0, 5, 0, 0, 3, 6],
                      [7, 0, 3, 0, 1, 8, 0, 0, 0]]

        self.buttons = [SolveButton("Solve", 70, 35, (174, 10), (209, 28), SudokuSolver(self.board)), ResetButton(
            "Reset", 70, 35, (294, 10), (329, 28), None), SkipButton("Skip", 70, 35, (414, 10), (449, 28), None)]

        self.sudoku_api = SudokuAPI(board)
        self.editable_cells = self.sudoku_api.getEmptyCells()

        # Board is shifted after we center it so we have to get the new coordinates to
        # Draw the board lines
        # centered_board_zero_x_cord = 54
        self.centered_board_zero_x_cord = self.sudoku_board.topleft[0]
        self.centered_board_width_cord = self.sudoku_board.topright[0]
        self.centered_board_height_cord = self.sudoku_board.bottomleft[1]

        # 540 width/height, 54 origin of centered sudoku board
        # 540/3 = 180 + 54 (origin) = 234
        # Second vertical line starting point = 234 = 180+180+54
        self.startBigSquares = self.centered_board_zero_x_cord + \
            SUDOKU_BOARD_LARGE_SQUARE_SIZE
        self.stopBigSquares = self.centered_board_zero_x_cord + \
            (SUDOKU_BOARD_LARGE_SQUARE_SIZE * 3)
        self.thickness = 4
        self.startSmallSquares = self.centered_board_zero_x_cord + \
            SUDOKU_BOARD_SMALL_SQUARE_SIZE
        self.stopSmallSquares = self.centered_board_zero_x_cord + \
            (SUDOKU_BOARD_SMALL_SQUARE_SIZE * 9)

    def getBoard(self):
        return self.sudoku_board

    def play(self, screen):
        updated_screen = self._setUp(screen)
        return updated_screen

    def _setUp(self, screen):

        screen = self._drawSudokuBoard(screen)
        return screen

    def _drawSudokuBoard(self, screen):
        # After screen fill so grid won't get overwritten
        for xcord in range(self.startBigSquares, self.stopBigSquares, SUDOKU_BOARD_LARGE_SQUARE_SIZE):
            pygame.draw.line(screen, BLACK, (xcord, self.centered_board_zero_x_cord),
                             (xcord, self.centered_board_width_cord), self.thickness)
            ycord = xcord
            pygame.draw.line(screen, BLACK, (self.centered_board_zero_x_cord, ycord),
                             (self.centered_board_width_cord, ycord), self.thickness)

        for xcord in range(self.startSmallSquares, self.stopSmallSquares, SUDOKU_BOARD_SMALL_SQUARE_SIZE):
            pygame.draw.line(screen, BLACK, (xcord, self.centered_board_zero_x_cord),
                             (xcord, self.centered_board_width_cord))
            ycord = xcord
            pygame.draw.line(screen, BLACK, (self.centered_board_zero_x_cord,
                                             ycord), (self.centered_board_width_cord, ycord))

        screen = self._drawButtons(screen)

        return screen

    def _drawButtons(self, screen):
        for button in self.buttons:
            pygame.draw.rect(screen, LIGHTBLUE, button.get_rect())
            textImage = self.font.render(button.get_text(), False, BLACK)
            buttonTextRect = textImage.get_rect(
                center=button.get_text_position())
            screen.blit(textImage, buttonTextRect)

        return screen

    def mouseClickEvent(self, click_pos):
        cellXCord = (
            click_pos[0] - self.centered_board_zero_x_cord) // SUDOKU_BOARD_SMALL_SQUARE_SIZE
        cellYCord = (
            click_pos[1] - self.centered_board_zero_x_cord) // SUDOKU_BOARD_SMALL_SQUARE_SIZE
        selection_pygame_coords = tuple((cellXCord, cellYCord))
        self._setSelectionPosition(selection_pygame_coords)
        self._setIsEditableCell(selection_pygame_coords)
        self._setClickedInsideBoard(click_pos)

        if click_pos:
            for button in self.buttons:
                button.on_click(click_pos)

    def _setSelectionPosition(self, selection_pygame_coords):
        self.selection_pos = toCenteredPygameCoordinates(
            selection_pygame_coords, self.centered_board_zero_x_cord)
        self._setSelectionRect()

    def _setSelectionRect(self):
        self.selection_rect = Rect(self.selection_pos, (60, 60))

    def _setIsEditableCell(self, selection_pygame_coords):
        self.is_editable_cell = 1 if selection_pygame_coords in self.editable_cells else 0

    def _setClickedInsideBoard(self, click_pos):
        # Use to check if we clicked inside the board or outside
        # If any of the coordinates are negative, we're outside the board
        # Also have to check for values larger than the width and height of the board
        areaClicked = (click_pos[
            0] - self.centered_board_zero_x_cord, self.centered_board_width_cord - click_pos[1])
        self.clicked_inside_board = True if (areaClicked[0] > 0 and areaClicked[1] > 0) and (
            areaClicked[0] < SUDOKU_BOARD_WIDTH and areaClicked[1] < SUDOKU_BOARD_WIDTH) else False

    def setFont(self, font):
        self.font = font
