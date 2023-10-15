import time

from app.windows.window import Window


class GameOverWindow(Window):
    def __init__(self, score: int):
        Window.__init__(self)
        self.window.timeout(999999)
        self.add_string_middle(f'Game Over, your score is {score}')
        time.sleep(2)
        self.add_string_bottom(f'Press any key to close window')
        self.window.getch()
