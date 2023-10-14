import sys

from app.windows.game_over_window import GameOverWindow
from app.windows.game_window import GameWindow
from app.windows.start_window import StartWindow
from exceptions import TooLowSize, ProportionsError

if __name__ == '__main__':
    try:
        StartWindow()
    except TooLowSize:
        sys.exit('Size of your terminal is too small, change the size and rerun app')
    try:
        window = GameWindow(0.3, 0.2, 777)
    except ProportionsError:
        sys.exit('Proportions are to big or to small!')
    while True:
        try:
            window.start_game()
        except UnboundLocalError:
            break
    GameOverWindow(window.score)
