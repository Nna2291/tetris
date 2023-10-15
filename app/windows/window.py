import curses

from exceptions import TooLowSize


class Window:
    def __init__(self):
        self.window = curses.initscr()
        # self.__window.clear()
        curses.echo()
        self.__y, self.__x = self.window.getmaxyx()
        if self.__x < 20 or self.__y < 20:
            raise TooLowSize()

        self.y_mid = self.__y // 2
        self.x_mid = self.__x // 2

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
            self.__y - delta_y - 1,
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

    def draw_field(self, y: int,
                   game: list[str]):
        self.window.clear()
        j = 0
        for i in range(y, y + len(game) + 1):
            try:
                self.add_string_middle_x(game[j], i)
            except IndexError:
                pass
            j += 1
        self.window.refresh()
