from Window import Window
from PointLine import Point, Line
from Cell import Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(50, 100, 50, 100, win)
    cell1.draw()
    cell2 = Cell(100, 150, 50, 100, win)
    cell2.draw()
    cell1.draw_move(cell2, True)
    win.wait_for_close()


main()
