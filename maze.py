from window import Window
from geometry import Point, Cell

from time import sleep


class Maze:
    def __init__(
            self,
            top_left: Point,
            num_rows: int,
            num_cols: int,
            window: Window,
            square_maze: bool = False,
    ) -> None:
        self._cells = []
        self._top_left = top_left
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._window = window
        dims = window.get_dimensions()
        vertical_pad = self._top_left.y
        horizontal_pad = self._top_left.x
        if square_maze:
            new_dims = min(dims), min(dims)
            self._top_left = Point(
                (dims[0] - new_dims[0]) // 2 + horizontal_pad,
                (dims[1] - new_dims[1]) // 2 + vertical_pad
            )
            dims = new_dims
        maze_width = dims[0] - 2 * horizontal_pad
        maze_height = dims[1] - 2 * vertical_pad
        self._cell_size_x = maze_width // num_cols
        self._cell_size_y = maze_height // num_rows
        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = []
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                cell_top_left = self._top_left + Point(j * self._cell_size_x, i * self._cell_size_y)
                cell_bottom_right = cell_top_left + Point(self._cell_size_x, self._cell_size_y)
                self._cells.append(
                    Cell(
                        self._window,
                        cell_top_left,
                        cell_bottom_right,
                        has_left_wall=True,
                        has_right_wall=True,
                        has_top_wall=True,
                        has_bottom_wall=True
                    )
                )
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        self._cells[i * self._num_cols + j].draw()
        self._animate()

    def _animate(self) -> None:
        self._window.redraw()
        sleep(0.05)
