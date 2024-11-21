class Point:
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    @property
    def coordinates(self) -> tuple[int, int]:
        return self.x, self.y
