from PointLine import Point, Line


class Cell:
    def __init__(self, x1, x2, y1, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._window = window

    def draw(self):
        if self.has_left_wall:
            self._window.draw_line(
                Line(
                    Point(self._x1, self._y1), Point(self._x1, self._y2)
                ),
                "black"
            )
        if self.has_right_wall:
            self._window.draw_line(
                Line(
                    Point(self._x2, self._y1), Point(self._x2, self._y2)
                ),
                "black"
            )
        if self.has_top_wall:
            self._window.draw_line(
                Line(
                    Point(self._x1, self._y1), Point(self._x2, self._y1)
                ),
                "black"
            )
        if self.has_bottom_wall:
            self._window.draw_line(
                Line(
                    Point(self._x1, self._y2), Point(self._x2, self._y2)
                ),
                "black"
            )
