class TooLowSize(Exception):
    def __init__(self):
        self.message = 'Size of your terminal is too small, change the size and rerun app'

    def __str__(self):
        return self.message
