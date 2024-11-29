from Window import Window
from PointLine import Point, Line


def main():
    win = Window(800, 600)
    line = Line(Point(50, 50), Point(150, 150))
    win.draw_line(line, "black")
    win.wait_for_close()


main()
