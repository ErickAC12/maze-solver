from Window import Window
from Maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(35, 15, 8, 10, 30, 30, win)
    win.wait_for_close()


main()
