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

        self.maximum_delta_x = 0

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

    # @staticmethod
    def append_to_string(self, prev_string: str,
                         text: str,
                         delta_x: int,
                         len_tetris_x: int, last_round: bool = False):
        string_mid = len(prev_string) // 2 + delta_x
        if abs(delta_x) >= len_tetris_x // 2 - len(text):
            delta_x = int(math.copysign(len_tetris_x // 2 - 2, delta_x))
            string_mid = len(prev_string) // 2 + delta_x
        first_ind = int(len(text) / 2)
        second_ind = math.ceil(len(text) / 2)

        change_string = prev_string[string_mid - first_ind:
                                    string_mid + second_ind + 1]

        with open('ans.txt', 'a') as f:
            f.write(f'{len(change_string) == len(text)}\n')
        if '#' in change_string and not last_round:
            raise ValueError
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
