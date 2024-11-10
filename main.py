from window import Window
from geometry import Line, Point, Cell
from maze import Maze


def main() -> None:
    window = Window(800, 800)
    # window.draw_line(Line(Point(0, 0), Point(800, 600)), "black")
    # window.draw_line(Line(Point(0, 600), Point(800, 0)), "red")
    # window.draw_line(Line(Point(300, 300), Point(400, 400)), "blue")
    # cell1 = Cell(window, Point(0, 10), Point(100, 100), True, True, True, True)
    # cell2 = Cell(window, Point(100, 0), Point(200, 100), True, True, True, False)
    # cell3 = Cell(window, Point(200, 100), Point(300, 100), False, True, False, True)
    # cell1.draw()
    # cell2.draw()
    # cell3.draw()
    # cell2.draw_move(cell3)
    # cell1.draw_move(cell2, undo=True)
    maze = Maze(
        Point(30, 30),
        10,
        10,
        window,
        # square_maze=True
    )
    window.wait_for_close()


if __name__ == "__main__":
    main()
