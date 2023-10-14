from app.windows.window import Window


class GameOverWindow(Window):
    def __init__(self, score: int):
        Window.__init__(self)
        self.add_string_middle(f'Game Over, your score is {score}')
