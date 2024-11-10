from tkinter import Canvas
from window import Window


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __floordiv__(self, other):
        return Point(self.x // other, self.y // other)


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str, width: int = 2) -> None:
        canvas.create_line(
            self.start.x,
            self.start.y,
            self.end.x,
            self.end.y,
            fill=fill_color,
            width=width
        )

class Cell:
    def __init__(
            self,
            window: Window,
            top_left: Point,
            bottom_right: Point,
            has_left_wall: bool,
            has_right_wall: bool,
            has_top_wall: bool,
            has_bottom_wall: bool
    ) -> None:
        self._window = window
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._top_right = Point(bottom_right.x, top_left.y)
        self._bottom_left = Point(top_left.x, bottom_right.y)
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self):
        if self.has_left_wall:
            self._window.draw_line(Line(self._top_left, self._bottom_left), "black")
        if self.has_right_wall:
            self._window.draw_line(Line(self._top_right, self._bottom_right), "black")
        if self.has_top_wall:
            self._window.draw_line(Line(self._top_left, self._top_right), "black")
        if self.has_bottom_wall:
            self._window.draw_line(Line(self._bottom_left, self._bottom_right), "black")

    def get_middle_point(self) -> Point:
        return (self._top_left + self._bottom_right) // 2

    def draw_move(self, to_cell: "Cell", undo: bool = False):
        fill_color: str = "gray"
        if not undo:
            fill_color = "red"
        self._window.draw_line(Line(self.get_middle_point(), to_cell.get_middle_point()), fill_color)
