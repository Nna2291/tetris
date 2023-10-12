import sys

from app.windows.window import Window
from exceptions import TooLowSize


class StartWindow(Window):
    def __init__(self):
        Window.__init__(self)
        self.add_string_middle('Tetris')
        self.add_string_middle('Programming laboratory work', delta_y=1)
        self.add_string_middle('Nefedov Nikolay IU7-11B', delta_y=2)
        self.add_string_bottom('Press any key to continue')
        self.window.getch()
