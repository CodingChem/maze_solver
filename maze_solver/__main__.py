from .modules.geometry import Cell, Window, Point, Maze


def main():
    w = Window(800, 600)
    m = Maze(100, 100, 500, 400, 10, 10, w)
    w.wait_to_close()


if __name__ == "__main__":
    main()
