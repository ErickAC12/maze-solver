from Cell import Cell
import random
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._seed = seed
        if self._seed is not None:
            random.seed(seed)
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        self._cells = [[None for _ in range(self._num_cols)] for _ in range(self._num_rows)]

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._cells[i][j] is None:
            x1 = self._x1 + j * self._cell_size_x
            x2 = x1 + self._cell_size_x
            y1 = self._y1 + i * self._cell_size_y
            y2 = y1 + self._cell_size_y
            self._cells[i][j] = Cell(x1, x2, y1, y2, self._window)
        if self._window is not None:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        self._window.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells[-1]) - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            directions = []
            if i > 0 and not self._cells[i-1][j].visited:
                directions.append((-1, 0))
            if i < self._num_rows - 1 and not self._cells[i+1][j].visited:
                directions.append((1, 0))
            if j > 0 and not self._cells[i][j-1].visited:
                directions.append((0, -1))
            if j < self._num_cols - 1 and not self._cells[i][j+1].visited:
                directions.append((0, 1))

            if not directions:
                self._draw_cell(i, j)
                return

            direction = random.choice(directions)
            next_i, next_j = i + direction[0], j + direction[1]

            if direction == (-1, 0):  # Up
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif direction == (1, 0):  # Down
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif direction == (0, -1):  # Left
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif direction == (0, 1):  # Right
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False

            self._break_walls_r(next_i, next_j)


    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
