import pygame
from constants import *
from pygame.locals import *

pygame.init()

font = pygame.font.SysFont(
    'arial', 35)

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
clickedInsideBoard = None
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
            editableCell = 0 if board[sudokuArrayCoordinates[0]
                                      ][sudokuArrayCoordinates[1]] > 0 else 1
            selectionRect = Rect(selectionPosition, (60, 60))

            # Use to check if we clicked inside the board or outside
            # If any of the coordinates are negative, we're outside the board
            # Also have to check for values larger than the width and height of the board
            areaClicked = (pygame.mouse.get_pos()[
                           0] - CENTERED_SUDOKU_ZERO_X_CORD, CENTERED_SUDOKU_HEIGHT_CORD - pygame.mouse.get_pos()[1])
            clickedInsideBoard = True if (areaClicked[0] > 0 and areaClicked[1] > 0) and (
                areaClicked[0] < SUDOKU_BOARD_WIDTH and areaClicked[1] < SUDOKU_BOARD_WIDTH) else False

        elif event.type == pygame.KEYDOWN:
            if selectionRect and clickedInsideBoard and editableCell and isInt(event.unicode):
                row = sudokuArrayCoordinates[0]
                col = sudokuArrayCoordinates[1]
                board[row][col] = int(event.unicode)

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

    # Draw numbers

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] != 0:
                cellNumber = str(board[row][col])
                textImage = font.render(cellNumber, False, BLACK)
                # flip the coordinates to match row/column positioning
                # x axis in pygame lines up in the same direction as grid column
                # y axis in pygame lines up in the same direction as grid row
                textPosition = ((col * SUDOKU_BOARD_SMALL_SQUARE_SIZE) + CENTERED_SUDOKU_ZERO_X_CORD,
                                (row * SUDOKU_BOARD_SMALL_SQUARE_SIZE) + CENTERED_SUDOKU_ZERO_X_CORD)

                # Ex: cell 4's position is 234, 54 so to center the text
                # Add 60 // 2 to the with and height of the cell to shift the image to the center
                # Center fo cell 4 would be 264, 84
                textPositionCentered = (
                    textPosition[0] + SUDOKU_BOARD_SMALL_SQUARE_SIZE // 2, textPosition[1] + SUDOKU_BOARD_SMALL_SQUARE_SIZE // 2)

                textRect = textImage.get_rect(center=textPositionCentered)

                screen.blit(
                    textImage, textRect)

    if selectionRect and clickedInsideBoard and editableCell:
        pygame.draw.rect(screen, RED, selectionRect, 2)

    pygame.display.update()

pygame.quit()
