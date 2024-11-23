from time import sleep
from .cell import Cell
from .window import Window
from .point import Point


class Maze:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        num_rows: int,
        num_cols: int,
        win: Window,
    ) -> None:
        self.cell_width = width // num_cols
        self.cell_height = height // num_rows
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._draw_cells()
        self._animate()

    def _create_cells(self):
        for height_index in range(self.num_rows):
            cel_col = []
            for width_index in range(self.num_cols):
                p1 = Point(
                    width_index * self.cell_width, height_index * self.cell_height
                )
                p2 = Point(
                    self.cell_width + width_index * self.cell_width,
                    self.cell_height + height_index * self.cell_height,
                )
                cel_col.append(Cell(self._win, p1, p2))
            self._cells.append(cel_col)

    def _draw_cells(self):
        for cel_col in self._cells:
            for cel in cel_col:
                cel.translate_cell(self.x, self.y)
                cel.draw()

    def _animate(self):
        while True:
            self._win.redraw()
            sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].walls["left"] = False
        self._cells[-1][-1].walls["right"] = False
