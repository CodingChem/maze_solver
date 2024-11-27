from time import sleep
from .cell import Cell
from .cell_wall import WallType
from .window import Window
from .point import Point
import random


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
        seed: int | None = None,
    ) -> None:
        if seed is not None:
            random.seed(seed)
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
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[-1][-1].has_right_wall = False

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            for neighbor in [
                x for x in self._get_adjecant_cells(i, j) if not x.visited
            ]:
                to_visit.append(neighbor)
            if len(to_visit) < 1:
                return
            target = random.choice(to_visit)
            current_cell.break_walls(target)
            target_i, target_j = self._get_cell_coordinates(target)
            self._break_walls_r(target_i, target_j)

    def _get_cell_coordinates(self, cell: Cell) -> tuple[int, int]:
        for i in range(len(self._cells)):
            if cell not in self._cells[i]:
                continue
            j = self._cells[i].index(cell)
            return i, j
        raise Exception("Cell not in grid!")

    def _get_adjecant_cells(self, i, j) -> list[Cell]:
        adjecant = []
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            try:
                adjecant.append(self._cells[i - x][j - y])
            except IndexError:
                continue
        return adjecant

    def _reset_cells_visited(self):
        for line in self._cells:
            for cell in line:
                cell.visited = False
