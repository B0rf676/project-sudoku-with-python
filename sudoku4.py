import sys
import clingo
from sudoku_board import Sudoku


class ClingoApp(clingo.application.Application):

    def main(self, ctl, files):

        ctl.load("sudoku.lp")

        for f in files:
            ctl.load(f)

        if not files:
            ctl.load("-")

        ctl.ground()
        ctl.solve()

    def print_model(self, model, printer) -> None:
        sudoku = Sudoku.from_model(model)
        print(sudoku)
        sys.stdout.flush()

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())