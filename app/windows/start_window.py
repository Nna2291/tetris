import curses

from exceptions import TooLowSize


class StartWindow:
    def __init__(self):
        self.window = curses.initscr()
        self.num_rows, self.num_cols = self.window.getmaxyx()
        if self.num_rows < 20 or self.num_cols < 20:
            raise TooLowSize()
        self.num_rows_mid = self.num_rows // 2
        self.num_cols_mid = self.num_cols // 2
        self.window.addstr(self.num_rows_mid, self.num_cols_mid - len('Tetris') // 2, 'Tetris')
        self.window.addstr(self.num_rows_mid + 1, self.num_cols_mid - len('Programming laboratory work') // 2,
                           'Programming laboratory work')
        self.window.addstr(self.num_rows_mid + 2, self.num_cols_mid - len('Nefedov Nikolay IU7-11B') // 2,
                           'Nefedov Nikolay IU7-11B')
        self.window.addstr(self.num_rows - 1, self.num_cols_mid - len('Press any key to continue') // 2,
                           'Press any key to continue')
        self.window.refresh()
        self.window.getch()
