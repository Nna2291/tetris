import sys

from app.windows.start_window import StartWindow
from app.windows.game_window import GameWindow
from exceptions import TooLowSize

if __name__ == '__main__':
    try:
        StartWindow()
    except TooLowSize:
        sys.exit('Size of your terminal is too small, change the size and rerun app')
    try:
        GameWindow(0.9, 0.9)
    except ValueError:
        sys.exit('Proportions are to big or to small!')
