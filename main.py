from Window import Window
from PointLine import Point, Line
from Cell import Cell


def main():
    win = Window(800, 600)
    cell = Cell(50, 100, 50, 100, win)
    cell.draw()
    win.wait_for_close()


main()
