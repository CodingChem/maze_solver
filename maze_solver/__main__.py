from .modules.geometry import Cell, Window, Point


def main():
    w = Window(800, 600)
    p1 = Point(50, 50)
    p2 = Point(100, 100)
    p3 = Point(150, 100)
    p4 = Point(100, 50)
    cell1 = Cell(w, p1, p2, True, False, True, True)
    cell2 = Cell(w, p4, p3, False, True, True, True)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2)
    w.wait_to_close()


if __name__ == "__main__":
    main()
