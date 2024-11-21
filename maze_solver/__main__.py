from .modules.cell import Cell
from .modules.window import Window
from .modules.point import Point


def main():
    w = Window(800, 600)
    p1 = Point(50, 50)
    p2 = Point(100, 100)
    cell = Cell(w, p1, p2, False, True, False, True)
    cell.draw()
    w.wait_to_close()


if __name__ == "__main__":
    main()
