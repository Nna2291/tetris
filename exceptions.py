class TooLowSize(Exception):
    def __init__(self):
        self.message = 'Size of your terminal is too small, change the size and rerun app'

    def __str__(self):
        return self.message


class ProportionsError(Exception):
    def __init__(self):
        self.message = 'Proportions are too big or too small!'

    def __str__(self):
        return self.message
