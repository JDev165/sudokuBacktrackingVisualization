import pygame
from pygame.locals import *

SCREEN_SIZE_DIVISIBLE_BY_NINE = 108
SCREEN_SIZE_MULTIPLIER = 6
SCREEN_WIDTH = SCREEN_SIZE_DIVISIBLE_BY_NINE * SCREEN_SIZE_MULTIPLIER
SCREEN_HEIGHT = SCREEN_SIZE_DIVISIBLE_BY_NINE * SCREEN_SIZE_MULTIPLIER
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SUDOKU_BOARD_OFFSET = SCREEN_SIZE_MULTIPLIER - 1
SUDOKU_BOARD_WIDTH = SCREEN_SIZE_DIVISIBLE_BY_NINE * SUDOKU_BOARD_OFFSET
SUDOKU_BOARD_HEIGHT = SCREEN_SIZE_DIVISIBLE_BY_NINE * SUDOKU_BOARD_OFFSET
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CENTER_SCREEN_X = SCREEN_SIZE[0] // 2
CENTER_SCREEN_Y = SCREEN_SIZE[1] // 2
SUDOKU_BOARD_SIZE = (SUDOKU_BOARD_WIDTH, SUDOKU_BOARD_HEIGHT)
SUDOKU_BOARD_LARGE_SQUARE_SIZE = SUDOKU_BOARD_WIDTH // 3
SUDOKU_BOARD_SMALL_SQUARE_SIZE = SUDOKU_BOARD_WIDTH // 9

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
sudoku_board = Rect(SUDOKU_BOARD_SIZE, SUDOKU_BOARD_SIZE)
sudoku_board.centery = CENTER_SCREEN_X
sudoku_board.centerx = CENTER_SCREEN_Y

# Board is shifted after we center it so we have to get the new coordinates to
# Draw the board lines
# CENTERED_SUDOKU_ZERO_X_CORD = 54
CENTERED_SUDOKU_ZERO_X_CORD = sudoku_board.topleft[0]
CENTERED_SUDOKU_WIDTH_CORD = sudoku_board.topright[0]
CENTERED_SUDOKU_HEIGHT_CORD = sudoku_board.bottomleft[1]

# 540 width/height, 54 origin of centered sudoku board
# 540/3 = 180 + 54 (origin) = 234
# Second vertical line starting point = 234 = 180+180+54
startSquares = CENTERED_SUDOKU_ZERO_X_CORD + SUDOKU_BOARD_LARGE_SQUARE_SIZE
stopSquares = CENTERED_SUDOKU_ZERO_X_CORD + \
    (SUDOKU_BOARD_LARGE_SQUARE_SIZE * 3)
startY = CENTERED_SUDOKU_ZERO_X_CORD + SUDOKU_BOARD_LARGE_SQUARE_SIZE
stopY = CENTERED_SUDOKU_ZERO_X_CORD + (SUDOKU_BOARD_LARGE_SQUARE_SIZE * 3)
incrementSquares = SUDOKU_BOARD_LARGE_SQUARE_SIZE
y1cord = CENTERED_SUDOKU_ZERO_X_CORD
y2cord = CENTERED_SUDOKU_WIDTH_CORD
x1cord = CENTERED_SUDOKU_ZERO_X_CORD
x2cord = CENTERED_SUDOKU_WIDTH_CORD
thicknessSquares = 4

startSmallSquares = CENTERED_SUDOKU_ZERO_X_CORD + SUDOKU_BOARD_SMALL_SQUARE_SIZE
stopSmallSquares = CENTERED_SUDOKU_ZERO_X_CORD + \
    (SUDOKU_BOARD_SMALL_SQUARE_SIZE * 9)
incrementSmallSquares = SUDOKU_BOARD_SMALL_SQUARE_SIZE

selectionPosition = None
sudokuArrayCoordinates = None
selectionRect = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                # the coordinate system in pygame
            cellXCord = (pygame.mouse.get_pos(
            )[0] - CENTERED_SUDOKU_ZERO_X_CORD) // SUDOKU_BOARD_SMALL_SQUARE_SIZE
            cellYCord = (pygame.mouse.get_pos(
            )[1] - CENTERED_SUDOKU_ZERO_X_CORD) // SUDOKU_BOARD_SMALL_SQUARE_SIZE

            selectionPosition = (
                (cellXCord * SUDOKU_BOARD_SMALL_SQUARE_SIZE) + CENTERED_SUDOKU_ZERO_X_CORD, (cellYCord * SUDOKU_BOARD_SMALL_SQUARE_SIZE) + CENTERED_SUDOKU_ZERO_X_CORD)
            # Need to convert pygame coordinates to the sudoku 2d array indexes
            # Just need to flip the coordinates
            # ycord = row, xcord = column in 2d array
            # Look at this when updating/pulling from 2d array
            sudokuArrayCoordinates = (cellYCord, cellXCord)
            print(selectionPosition)
            selectionRect = Rect(selectionPosition, (60, 60))

    pygame.display.set_caption("Sudoku")
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, sudoku_board, 1)

    # After screen fill so grid won't get overwritten
    for xcord in range(startSquares, stopSquares, incrementSquares):
        pygame.draw.line(screen, BLACK, (xcord, y1cord),
                         (xcord, y2cord), thicknessSquares)
        ycord = xcord
        pygame.draw.line(screen, BLACK, (x1cord, ycord),
                         (x2cord, ycord), thicknessSquares)

    for xcord in range(startSmallSquares, stopSmallSquares, incrementSmallSquares):
        pygame.draw.line(screen, BLACK, (xcord, y1cord), (xcord, y2cord))
        ycord = xcord
        pygame.draw.line(screen, BLACK, (x1cord, ycord), (x2cord, ycord))

    if selectionRect:
        pygame.draw.rect(screen, RED, selectionRect, 2)
    pygame.display.update()

pygame.quit()
