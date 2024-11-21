from maze_solver.modules.line import Line
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

    def draw(self):
        for line in self.get_walls():
            line.draw(self._win.canvas, "black")

    def get_walls(self) -> list[Line]:
        return [x for x in self.walls.values() if x is not None]

    @property
    def has_left_wall(self):
        return self.walls["left"] is not None

    @has_left_wall.setter
    def has_left_wall(self, arg: bool):
        if arg:
            self.walls["left"] = Line(self.upper_left, self.bottom_left)
        else:
            self.walls["left"] = None

    @property
    def has_right_wall(self):
        return self.walls["right"] is not None

    @has_right_wall.setter
    def has_right_wall(self, arg: bool):
        if arg:
            self.walls["right"] = Line(self.upper_right, self.bottom_right)
        else:
            self.walls["right"] = None

    @property
    def has_top_wall(self):
        return self.walls["top"] is not None

    @has_top_wall.setter
    def has_top_wall(self, arg: bool):
        if arg:
            self.walls["top"] = Line(self.upper_left, self.upper_right)
        else:
            self.walls["top"] = None

    @property
    def has_bottom_wall(self):
        return self.walls["bottom"] is not None

    @has_bottom_wall.setter
    def has_bottom_wall(self, arg: bool):
        if arg:
            self.walls["bottom"] = Line(self.bottom_left, self.bottom_right)
        else:
            self.walls["bottom"] = None
