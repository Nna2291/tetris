import curses
import random
import time

from app.data.figures import figures


# window = curses.initscr()
# figure = random.choice(figures)
# figure_line = figure.split('\n')
# for i in range(len(figure_line)):
#     window.addstr(i, 0, figure_line[i])
#     window.refresh()
# time.sleep(0.5)
# for i in range(1, 20):
#     window.clear()
#     for j in range(len(figure_line)):
#         window.addstr(i + j, 0, figure_line[j])
#     window.refresh()
#     time.sleep(0.5)
#     window.refresh()


class GameWindow:
    def __init__(self, y_proportions: float, x_proportions: float):
        self.window = curses.initscr()
        # self.window = curses.newwin()
        self.window.clear()
        if not (0.5 <= y_proportions <= 0.9) or not (0.5 <= x_proportions <= 0.9):
            raise ValueError('Proportions are to big or to small!')
        self.y, self.x = self.window.getmaxyx()
        self.len_tetris_y = int(self.y * y_proportions)
        self.len_tetris_x = int(self.x * x_proportions)
        self.x_free_space = (self.x - self.len_tetris_x) // 2
        self.y_free_space = (self.y - self.len_tetris_y) // 2
        for i in range(self.y_free_space, self.y - self.y_free_space):
            if i == self.y - self.y_free_space - 1:
                self.window.addstr(i, 0, ' ' * self.x_free_space + '*' * self.len_tetris_x + ' ' * self.x_free_space)
            else:
                self.window.addstr(i, 0, ' ' * self.x_free_space +
                                   '|' + ' ' * (self.len_tetris_x - 2) +
                                   '|' + ' ' * self.x_free_space)
            self.window.refresh()
        c = self.window.getch()
        print(chr(c))

    @staticmethod
    def generate_figure():
        return random.choice(figures).split('\n')
