class WordFilter(object):
    def __init__(self, mode, letter, index):
        # Mode can be green/yellow/black
        self.mode = mode
        self.letter = letter
        self.index = index

    def __str__(self):
        return f"{self.letter.upper()} - {self.mode.upper()}"
