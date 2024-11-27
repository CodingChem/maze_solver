from enum import Enum
from tkinter import Canvas
from .line import Line
from .point import Point


class WallType(Enum):
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"


class CellWall(Line):
    def __init__(self, p1: Point, p2: Point, exists: bool) -> None:
        super().__init__(p1, p2)
        self.exists = exists

    def draw(self, canvas: Canvas, fill_color: str | None):
        if fill_color:
            return super().draw(canvas, fill_color)
        return super().draw(canvas, "black" if self.exists else "white")

    def iswall(self):
        return self.exists

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, CellWall):
            return False
        return super().__eq__(value)
