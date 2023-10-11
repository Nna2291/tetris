import curses

from exceptions import TooLowSize


class Window:
    def __init__(self):
        self.window = curses.initscr()
        self.y, self.x = self.window.getmaxyx()
        if self.x < 20 or self.y < 20:
            raise TooLowSize()

        self.y_mid = self.y // 2
        self.x_mid = self.x // 2

    def add_string_middle(self, text: str,
                          delta_x: int = 0,
                          delta_y: int = 0):
        self.window.addstr(
            self.y_mid + delta_y,
            (self.x_mid - len(text) // 2) + delta_x,
            text
        )
        self.window.refresh()

    def add_string_bottom(self, text: str,
                          delta_x: int = 0,
                          delta_y: int = 0):
        self.window.addstr(
            self.y - delta_y-1,
            (self.x_mid - len(text) // 2) + delta_x,
            text
        )
