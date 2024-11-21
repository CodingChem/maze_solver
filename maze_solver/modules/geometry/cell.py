from __future__ import annotations
from .line import Line
from .point import Point
from .window import Window


class Cell:
    def __init__(
        self,
        win: Window,
        upper_left: Point,
        bottom_right: Point,
        has_left_wall: bool,
        has_right_wall: bool,
        has_top_wall: bool,
        has_bottom_wall: bool,
    ):
        self.upper_left = upper_left
        self.bottom_right = bottom_right
        self.upper_right = Point(bottom_right.x, upper_left.y)
        self.bottom_left = Point(upper_left.x, bottom_right.y)
        self.walls = {}
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._win = win

    def draw(self) -> None:
        for line in self.get_walls():
            line.draw(self._win.canvas, "black")

    def get_walls(self) -> list[Line]:
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
    def has_left_wall(self) -> bool:
        return self.walls["left"] is not None

    @has_left_wall.setter
    def has_left_wall(self, arg: bool) -> None:
        if arg:
            self.walls["left"] = Line(self.upper_left, self.bottom_left)
        else:
            self.walls["left"] = None

    @property
    def has_right_wall(self) -> bool:
        return self.walls["right"] is not None

    @has_right_wall.setter
    def has_right_wall(self, arg: bool) -> None:
        if arg:
            self.walls["right"] = Line(self.upper_right, self.bottom_right)
        else:
            self.walls["right"] = None

    @property
    def has_top_wall(self) -> bool:
        return self.walls["top"] is not None

    @has_top_wall.setter
    def has_top_wall(self, arg: bool) -> None:
        if arg:
            self.walls["top"] = Line(self.upper_left, self.upper_right)
        else:
            self.walls["top"] = None

    @property
    def has_bottom_wall(self) -> bool:
        return self.walls["bottom"] is not None

    @has_bottom_wall.setter
    def has_bottom_wall(self, arg: bool) -> None:
        if arg:
            self.walls["bottom"] = Line(self.bottom_left, self.bottom_right)
        else:
            self.walls["bottom"] = None
