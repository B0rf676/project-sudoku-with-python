from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""

        for r in range(1, 10):
            for c in range(1, 10):
                s += str(self.sudoku[(r, c)]) + " "
                if c in (3, 6):
                    s += ' '
            s += '\n'
            if r in (3, 6):
                s += '\n'
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}

        for a in model.symbols(shown=True):
            if a.name == "sudoku":
                r = a.arguments[0].number
                c = a.arguments[1].number
                v = a.arguments[2].number
                sudoku[(r, c)] = v

        return cls(sudoku)
