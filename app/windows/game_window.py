import curses
import random

from app.data.figures import figures
from app.windows.window import Window
from exceptions import ProportionsError


class GameWindow(Window):
    def __init__(self, y_proportions: float,
                 x_proportions: float,
                 delay_time: int = 750):
        if not (0.1 <= y_proportions <= 0.9) or not (0.1 <= x_proportions <= 0.9):
            raise ProportionsError()

        Window.__init__(self)

        self.score = 0
        self.game_field = []

        self.window = curses.initscr()
        self.window.clear()
        self.window.timeout(delay_time)

        self.y, self.x = self.window.getmaxyx()
        self.len_tetris_y = int(self.y * y_proportions)
        self.len_tetris_x = int(self.x * x_proportions)
        self.x_free_space = (self.x - self.len_tetris_x) // 2
        self.y_free_space = (self.y - self.len_tetris_y) // 2

        for i in range(self.y_free_space, self.y - self.y_free_space):
            if i == self.y - self.y_free_space - 1:
                self.add_string_middle_x('*' * self.len_tetris_x, i)
                self.game_field.append('*' * self.len_tetris_x)
            elif i == 0:
                self.add_string_middle_x(' ' * self.len_tetris_x, i)
                self.game_field.append(' ' * self.len_tetris_x)
            else:
                self.add_string_middle_x('|' + ' ' * (self.len_tetris_x - 2) + '|', i)
                self.game_field.append('|' + ' ' * (self.len_tetris_x - 2) + '|')
        # breakpoint()

    @staticmethod
    def generate_figure():
        return random.choice(figures).split('\n')

    @staticmethod
    def find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    @staticmethod
    def turn_figure(figure: list[str]):
        new_fig = []
        count = len(max(figure, key=len))

        print(new_fig)
        for i in range(count):
            string = ''
            for j in range(len(figure)):
                string += figure[j][i]
            new_fig.append(string)
        new_fig.reverse()
        new_fig.append('')
        return new_fig

    def add_figure(self,
                   figure: list[str],
                   delta_x: int,
                   delta_y: int):
        field = self.game_field.copy()

        j = -1
        for i in range(delta_y, delta_y + len(figure)):
            j += 1

            line_in_list = list(field[i])
            figure_line = figure[j]
            middle_index = len(field[1]) // 2 + delta_x
            end_index = middle_index + len(figure_line)

            figure_line = list(figure_line)

            if '*' in line_in_list[middle_index:end_index]:
                raise IndexError
            if '#' in line_in_list[middle_index:end_index]:
                sharp_indexes = self.find(line_in_list[middle_index:end_index], '#')
                for index in sharp_indexes:
                    if figure_line[index] != ' ':
                        raise IndexError
                    else:
                        figure_line[index] = '#'

            line_in_list[middle_index:end_index] = figure_line
            if line_in_list.count('|') != 2 and '*' not in line_in_list:
                if line_in_list[0] != '|':
                    line_in_list[0] = '|'
                    line_in_list[1:len(figure_line) + 1] = figure_line
                    delta_x += 1
                else:
                    len_line = len(line_in_list)
                    line_in_list[-1] = '|'
                    line_in_list[len_line - len(figure_line) - 1:len_line - 1] = figure_line
                    delta_x -= 1
            field[i] = ''.join(line_in_list)
        return field, delta_x

    def check_field(self):
        field = self.game_field

        for i, el in enumerate(field):
            if el.count('#') != len(el) - 2:
                continue
            del field[i]
            field[0] = '|' + ' ' * (self.len_tetris_x - 2) + '|'
            field.insert(0, '     ')
            self.score += 1
        self.draw_field(self.y_free_space, self.game_field)

    def start_game(self):
        figure = self.generate_figure()
        i = 0
        delta_x = 0
        while True:
            ch = self.window.getch()
            if ch == -1:
                pass
            elif chr(ch) == 'a':
                delta_x += -1
                i -= 1
            elif chr(ch) == 'd':
                delta_x += 1
                i -= 1
            elif chr(ch) == 'q':
                figure = self.turn_figure(figure[0:len(figure) - 1])
            try:
                temp_field, delta_x = self.add_figure(
                    figure,
                    delta_x,
                    i
                )
                self.draw_field(self.y_free_space, temp_field)
                i += 1
            except IndexError:
                self.game_field = temp_field
                self.check_field()
                break
