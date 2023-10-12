import sys

from app.windows.start_window import StartWindow
# import app.windows.game_window
from app.windows.game_window import GameWindow
from exceptions import TooLowSize, ProportionsError

if __name__ == '__main__':
    try:
        StartWindow()
    except TooLowSize:
        sys.exit('Size of your terminal is too small, change the size and rerun app')
    try:
        window = GameWindow(0.9, 0.9, 700)
        window.run_game()
    except ProportionsError:
        sys.exit('Proportions are to big or to small!')
    