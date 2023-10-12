import curses
import random

from app.data.figures import figures
from app.windows.window import Window
from exceptions import ProportionsError


class GameWindow(Window):
    def __init__(self, y_proportions: float,
                 x_proportions: float,
                 delay_time: int = 750):
        Window.__init__(self)
        self.window = curses.initscr()
        self.window.clear()
        self.window.timeout(delay_time)
        if not (0.5 <= y_proportions <= 0.9) or not (0.5 <= x_proportions <= 0.9):
            raise ProportionsError()
        self.y, self.x = self.window.getmaxyx()
        self.speed = 0.2
        self.len_tetris_y = int(self.y * y_proportions)
        self.len_tetris_x = int(self.x * x_proportions)
        self.x_free_space = (self.x - self.len_tetris_x) // 2
        self.y_free_space = (self.y - self.len_tetris_y) // 2

    @staticmethod
    def generate_figure():
        return random.choice(figures).split('\n')

    def draw_figure(self, game: list[str],
                    figure: list[str],
                    delta_x: int,
                    delta_y: int):
        figure_y = len(figure)
        j = -1

        for i in range(self.y_free_space, self.y_free_space + delta_y):
            line = '|' + ' ' * (self.len_tetris_x - 2) + '|'
            self.add_string_middle_x(line, i)
            game[i] = line
        for i in range(self.y_free_space + delta_y,
                       self.y_free_space + figure_y + delta_y):
            j += 1
            elemnt_figure = figure[j]
            new_string = self.append_to_string(
                game[i],
                elemnt_figure,
                delta_x
            )
            game[i] = new_string
        return game

    def run_game(self):
        figure = self.generate_figure()
        game = []
        delta_x = 0
        for i in range(self.y_free_space, self.y - self.y_free_space):
            if i == self.y - self.y_free_space - 1:
                self.add_string_middle_x('*' * self.len_tetris_x, i)
                game.append('*' * self.len_tetris_x)
            else:
                self.add_string_middle_x('|' + ' ' * (self.len_tetris_x - 2) + '|', i)
                game.append('|' + ' ' * (self.len_tetris_x - 2) + '|')
        for i in range(self.y + 10):
            ch = self.window.getch()
            if ch == -1:
                pass
            elif chr(ch) == 'a':
                delta_x += -1
            elif chr(ch) == 'd':
                delta_x += 1
            game = self.draw_figure(game,
                                    figure,
                                    delta_x,
                                    (len(figure) + 1 * i) + 1)
            self.draw_field(self.y, self.y_free_space, game)
