from tkinter import Canvas
from .point import Point


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Line):
            return False
        return (self.p1 == value.p1 and self.p2 == value.p2) or (
            self.p1 == value.p2 and self.p2 == value.p1
        )
