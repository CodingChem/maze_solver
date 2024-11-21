class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @property
    def coordinates(self) -> tuple[int, int]:
        return self.x, self.y
