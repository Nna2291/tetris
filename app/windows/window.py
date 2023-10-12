import curses
import math

from exceptions import TooLowSize


class Window:
    def __init__(self):
        self.window = curses.initscr()
        curses.echo()
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
            self.y - delta_y - 1,
            (self.x_mid - len(text) // 2) + delta_x,
            text
        )
        self.window.refresh()

    def add_string_middle_x(self, text: str,
                            y: int = 0):
        self.window.addstr(
            y,
            self.x_mid - len(text) // 2,
            text
        )
        self.window.refresh()

    @staticmethod
    def append_to_string(prev_string: str,
                         text: str,
                         delta_x: int):
        string_mid = len(prev_string) // 2 + delta_x
        first_ind = int(len(text) / 2)
        second_ind = math.ceil(len(text) / 2)
        new_string = (prev_string[0:string_mid - first_ind] +
                      text +
                      prev_string[string_mid + second_ind:])
        return new_string

    def draw_field(self, y: int,
                   free_y: int,
                   game: list[str]):
        self.window.clear()
        for i in range(free_y, y - free_y):
            try:
                self.add_string_middle_x(game[i], i)
            except IndexError:
                pass
        self.window.refresh()
