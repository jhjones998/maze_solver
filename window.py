from tkinter import Tk, BOTH, Canvas
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geometry import Line


class Window:
    def __init__(self, width: int, height: int) -> None:
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, width=width, height=height, bg="white")
        self._canvas.pack()
        self._window_running = False

    def redraw(self) -> None:
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self) -> None:
        self._window_running = True
        while self._window_running:
            self.redraw()

    def close(self) -> None:
        self._window_running = False
        self._root.destroy()

    def draw_line(self, line: "Line", fill_color: str):
        line.draw(self._canvas, fill_color=fill_color)

    def get_dimensions(self) -> tuple[int, int]:
        return int(self._canvas["width"]), int(self._canvas["height"])
