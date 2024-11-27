from __future__ import annotations
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
        self.walls = {}
        self.set_pos(upper_left, bottom_right)
        self.set_walls(has_left_wall, has_right_wall, has_top_wall, has_bottom_wall)
        self._win = win
        self.visited = False

    def break_walls(self, target: Cell) -> None:
        # case: target is to the LEFT
        if self.walls[WallType.LEFT] == target.walls[WallType.RIGHT]:
            self.has_left_wall = False
            target.has_right_wall = False
            return
        # case: target is to the RIGHT
        if self.walls[WallType.RIGHT] == target.walls[WallType.LEFT]:
            self.has_right_wall = False
            target.has_left_wall = False
            return
        # case: target is on the TOP
        if self.walls[WallType.TOP] == target.walls[WallType.BOTTOM]:
            self.has_top_wall = False
            target.has_bottom_wall = False
            return
        # case: target is on the BOTTOM
        if self.walls[WallType.BOTTOM] == target.walls[WallType.TOP]:
            self.has_bottom_wall = False
            target.has_top_wall = False
            return

    def draw(self) -> None:
        for wall in self.get_walls():
            wall.draw(self._win.canvas, None)

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
        self.walls[WallType.TOP] = CellWall(
            self.upper_left, self.upper_right, self.has_top_wall
        )
        self.walls[WallType.BOTTOM] = CellWall(
            self.bottom_left, self.bottom_right, self.has_bottom_wall
        )
        self.walls[WallType.LEFT] = CellWall(
            self.upper_left, self.bottom_left, self.has_left_wall
        )
        self.walls[WallType.RIGHT] = CellWall(
            self.upper_right, self.bottom_right, self.has_right_wall
        )

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

    def get_walls(self) -> list[CellWall]:
        return [x for x in self.walls.values()]

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
        if WallType.LEFT not in self.walls:
            return False
        return self.walls[WallType.LEFT].iswall()

    @has_left_wall.setter
    def has_left_wall(self, arg: bool):
        self.walls[WallType.LEFT].exists = arg

    @property
    def has_right_wall(self):
        if WallType.RIGHT not in self.walls:
            return False
        return self.walls[WallType.RIGHT].iswall()

    @has_right_wall.setter
    def has_right_wall(self, arg: bool):
        self.walls[WallType.RIGHT].exists = arg

    @property
    def has_top_wall(self):
        if WallType.TOP not in self.walls:
            return False
        return self.walls[WallType.TOP].iswall()

    @has_top_wall.setter
    def has_top_wall(self, arg: bool):
        self.walls[WallType.TOP].exists = arg

    @property
    def has_bottom_wall(self):
        if WallType.BOTTOM not in self.walls:
            return False
        return self.walls[WallType.BOTTOM].iswall()

    @has_bottom_wall.setter
    def has_bottom_wall(self, arg: bool):
        self.walls[WallType.BOTTOM].exists = arg
