class Sudoku:
    def __init__(self, board):
        self._board = board

    def getBoard(self):
        return self._board

    def solve(self):
        # Will handle the backtracking
        nextEmptyCell = self._getNextEmptyCell()
        if nextEmptyCell == None:
            return True

        # Try all numbers from 1 to 9
        for numberToTry in range(1, 10):
            if self._isValid(nextEmptyCell, numberToTry):
                # Set to numberToTry if valid
                self._board[nextEmptyCell[0]][nextEmptyCell[1]] = numberToTry
                if self.solve():
                    return True
                # Backtrack and reset the previous value if next recursive call returns False
                self._board[nextEmptyCell[0]][nextEmptyCell[1]] = 0
        return False

    def _getNextEmptyCell(self):
        emptyCellLocation = None
        for row in range(len(self._board)):
            for col in range(len(self._board)):
                if self._board[row][col] == 0:
                    emptyCellLocation = (row, col)
        return emptyCellLocation

    def isValid(self, emptyCellLocation: tuple, numberToTry: int):
        # Return validVertically and validHorizontally and validSubgrid
        validNumber = self._validVertically(emptyCellLocation, numberToTry) and self._validHorizontally(
            emptyCellLocation, numberToTry) and self._validSubgrid(emptyCellLocation, numberToTry)
        return validNumber

    def _validVertically(self, emptyCellLocation: tuple, numberToTry: int):
        columnIndex = emptyCellLocation[1]
        valid = True
        for row in range(len(self._board)):
            if self._board[row][columnIndex] == numberToTry:
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

    def print(self):
        pass


def main():
    board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
             [6, 8, 0, 0, 7, 0, 0, 9, 0],
             [1, 9, 0, 0, 0, 4, 5, 0, 0],
             [8, 2, 0, 1, 0, 0, 0, 4, 0],
             [0, 0, 4, 6, 0, 2, 9, 0, 0],
             [0, 5, 0, 0, 0, 3, 0, 2, 8],
             [0, 0, 9, 3, 0, 0, 0, 7, 4],
             [0, 4, 0, 0, 5, 0, 0, 3, 6],
             [7, 0, 3, 0, 1, 8, 0, 0, 0]]

    solution = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
                [6, 8, 2, 5, 7, 1, 4, 9, 3],
                [1, 9, 7, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 6, 8, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 5, 9]]


if __name__ == "__main__":
    main()
