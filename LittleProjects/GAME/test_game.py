import Game
import numpy as np

sudoku = np.array([[8, 9, 1, 5, 7, 0, 0, 0, 0],
                   [4, 0, 7, 0, 1, 8, 9, 0, 0],
                   [0, 0, 0, 4, 0, 9, 1, 8, 7],
                   [6, 0, 0, 0, 0, 0, 0, 3, 8],
                   [0, 5, 4, 6, 0, 1, 0, 9, 0],
                   [7, 0, 0, 2, 0, 0, 4, 0, 0],
                   [0, 0, 0, 8, 9, 3, 0, 0, 4],
                   [5, 4, 3, 0, 0, 0, 0, 0, 9],
                   [0, 2, 0, 1, 5, 0, 0, 0, 6]])


def test_quadrant_0():
    assert (Game.check_quadrant(sudoku, 1, 0, 5) is False)


def test_quadrant_1():
    assert (Game.check_quadrant(sudoku, 2, 0, 5) is True)


def test_row_0():
    assert (Game.check_row(sudoku, 1, 0) is False)


def test_row_1():
    assert (Game.check_row(sudoku, 2, 0) is True)


def test_col_0():
    assert (Game.check_column(sudoku, 1, 5) is False)


def test_col_1():
    assert (Game.check_column(sudoku, 2, 5) is True)


def test_index_0():
    assert (Game.indexes(sudoku) == (0, 5))


def test_index_1():
    sudoku[0][0] = 0
    assert (Game.indexes(sudoku) == (0, 0))


def test_solution():
    assert (Game.solution(sudoku) is True)


