class SudokuAPI:
    def __init__(self, board):
        self._board = board

    def updateCell(self, cell: tuple, value: int):
        self._board[cell[0]][cell[1]] = value

    def isValid(self, emptyCellLocation: tuple, numberToTry: int):
        # Return validVertically and validHorizontally and validSubgrid
        validNumber = self._validVertically(emptyCellLocation, numberToTry) and self._validHorizontally(
            emptyCellLocation, numberToTry) and self._validSubgrid(emptyCellLocation, numberToTry)
        return validNumber

    def _validVertically(self, emptyCellLocation: tuple, numberToTry: int):
        column = emptyCellLocation[1]
        valid = True
        for row in range(len(self._board)):
            if self._board[row][column] == numberToTry:
                valid = False
                break
        return valid

    def _validHorizontally(self, emptyCellLocation: tuple, numberToTry: int):
        rowIndex = emptyCellLocation[0]
        rowToCheck = self._board[rowIndex]
        valid = True if numberToTry not in rowToCheck else False
        return valid

    def _validSubgrid(self, emptyCellLocation: tuple, numberToTry: int):
        subgrid_row = (emptyCellLocation[0] // 3) * 3
        subgrid_col = (emptyCellLocation[1] // 3) * 3
        for row in range(0, 3):
            for col in range(0, 3):
                if self._board[subgrid_row + row][subgrid_col + col] == numberToTry:
                    return False
        return True

    def getEmptyCells(self):
        editableCells = []
        for row in range(len(self._board)):
            for col in range(len(self._board)):
                if self._board[row][col] == 0:
                    editableCells.append((row, col))

        return editableCells
