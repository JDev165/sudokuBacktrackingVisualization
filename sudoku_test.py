import unittest
import warnings
from sudoku import Sudoku

board1 = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
          [6, 8, 0, 0, 7, 0, 0, 9, 0],
          [1, 9, 0, 0, 0, 4, 5, 0, 0],
          [8, 2, 0, 1, 0, 0, 0, 4, 0],
          [0, 0, 4, 6, 0, 2, 9, 0, 0],
          [0, 5, 0, 0, 0, 3, 0, 2, 8],
          [0, 0, 9, 3, 0, 0, 0, 7, 4],
          [0, 4, 0, 0, 5, 0, 0, 3, 6],
          [7, 0, 3, 0, 1, 8, 0, 0, 0]]


class TestSudoku(unittest.TestCase):

    def test_solve(self):
        pass

    def test_get_next_empty(self):
        sudokuToSolve = Sudoku(board1)
        nextEmptyCell = sudokuToSolve.getNextEmptyCell()
        self.assertTrue((8, 8) == nextEmptyCell)

    def test_is_valid(self):
        pass

    def test_valid_vertically(self):
        pass

    def test_valid_horizontally(self):
        pass

    def test_valid_subgrid(self):
        pass


def main():
    test = TestSudoku()
    test.test_get_next_empty()


if __name__ == "__main__":
    main()
