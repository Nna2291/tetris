import curses
import random

from app.config import FIGURES
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
        self.__y, self.__x = self.window.getmaxyx()
        self.__game_field = []
        self.__window = curses.initscr()
        self.__window.clear()
        self.__window.timeout(delay_time)

        self.__len_tetris_y = int(self.__y * y_proportions)
        self.__len_tetris_x = int(self.__x * x_proportions)
        self.__x_free_space = (self.__x - self.__len_tetris_x) // 2
        self.__y_free_space = (self.__y - self.__len_tetris_y) // 2

        for i in range(self.__y_free_space, self.__y - self.__y_free_space):
            if i == self.__y - self.__y_free_space - 1:
                self.add_string_middle_x('*' * self.__len_tetris_x, i)
                self.__game_field.append('*' * self.__len_tetris_x)
            else:
                self.add_string_middle_x('|' + ' ' * (self.__len_tetris_x - 2) + '|', i)
                self.__game_field.append('|' + ' ' * (self.__len_tetris_x - 2) + '|')
        # breakpoint()

    @staticmethod
    def generate_figure():
        return random.choice(FIGURES).split('\n')

    @staticmethod
    def find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def find_empty_spaces(self):
        field = self.__game_field.copy()
        fiel = list(filter(lambda x: set(list(x)) == {' ', '|'}, field))
        return len(fiel)

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
        field = self.__game_field.copy()
        empty_spaces = self.find_empty_spaces()
        if empty_spaces <= len(figure):
            raise UnboundLocalError
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
        field = self.__game_field

        for i, el in enumerate(field):
            if el.count('#') != len(el) - 2:
                continue
            del field[i]
            field[0] = '|' + ' ' * (self.__len_tetris_x - 2) + '|'
            # field.insert(0, '     ')
            self.score += 1
        self.draw_field(self.__y_free_space, self.__game_field)

    def start_game(self):
        figure = self.generate_figure()
        i = 0
        delta_x = 0
        while True:
            ch = self.__window.getch()
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
                self.draw_field(self.__y_free_space, temp_field)
                i += 1
            except IndexError:
                try:
                    self.__game_field = temp_field
                    self.check_field()
                except UnboundLocalError:
                    pass
                break

    def close_window(self):
        self.__window.clear()
        curses.endwin()
