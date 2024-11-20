from modules.window import Window
from modules.point import Point
from modules.line import Line


def main():
    w = Window(800, 600)
    p1 = Point(20, 50)
    p2 = Point(50, 20)
    line = Line(p1, p2)
    line.draw(w.canvas, "black")
    w.wait_to_close()


if __name__ == "__main__":
    main()
