from __future__ import annotations
from .line import Line
from .point import Point
from .window import Window
from .cell_wall import CellWall, WallType


class Cell:
    def __init__(
        self,
        win: Window,
        upper_left: Point,
        bottom_right: Point,
        has_left_wall: bool = True,
        has_right_wall: bool = True,
        has_top_wall: bool = True,
        has_bottom_wall: bool = True,
    ):
        self.walls = {
            WallType.LEFT: None,
            WallType.RIGHT: None,
            WallType.TOP: None,
            WallType.BOTTOM: None,
        }
        self.set_pos(upper_left, bottom_right)
        self.set_walls(has_left_wall, has_right_wall, has_top_wall, has_bottom_wall)
        self._win = win

    def draw(self) -> None:
        for line in self.get_walls():
            line[0].draw(self._win.canvas, line[1])

    def set_walls(self, lw: bool, rw: bool, tw: bool, bw: bool):
        self.has_left_wall = lw
        self.has_right_wall = rw
        self.has_top_wall = tw
        self.has_bottom_wall = bw

    def set_pos(self, upper_left: Point, bottom_right: Point):
        self.upper_left = upper_left
        self.bottom_right = bottom_right
        self.upper_right = Point(bottom_right.x, upper_left.y)
        self.bottom_left = Point(upper_left.x, bottom_right.y)

    def translate_cell(self, x_off: int, y_off: int):
        new_upper_left = Point(self.upper_left.x + x_off, self.upper_left.y + y_off)
        new_bottom_right = Point(
            self.bottom_right.x + x_off, self.bottom_right.y + y_off
        )
        self.set_pos(new_upper_left, new_bottom_right)
        self.set_walls(
            self.has_left_wall,
            self.has_right_wall,
            self.has_top_wall,
            self.has_bottom_wall,
        )

    def get_walls(self) -> list[tuple[Line, str]]:
        return [x for x in self.walls.values() if x is not None]

    def get_center(self) -> Point:
        return Point(
            (self.upper_left.x + self.bottom_right.x) // 2,
            (self.bottom_left.y + self.upper_right.y) // 2,
        )

    def draw_move(self, to_cell: Cell, undo=False) -> None:
        self._win.canvas.create_line(
            *self.get_center().coordinates,
            *to_cell.get_center().coordinates,
            fill="gray" if undo else "red",
        )

    @property
    def has_left_wall(self):
        return self.walls[WallType.LEFT].iswall()
