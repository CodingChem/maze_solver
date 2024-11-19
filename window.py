from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.geometry = f"{width}x{height}"  # pyright: ignore
        self.root.title = "Maze Solver"  # pyright: ignore
        self.canvas = Canvas(self.root)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_to_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False


if __name__ == "__main__":
    w = Window(800, 600)
    w.root.mainloop()
