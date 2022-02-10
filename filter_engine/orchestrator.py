from filter_engine.filters import WordFilter


class Orchestrator(object):
    def __init__(self):
        self.word_list = list()
        self.master_list = list()
        self.filter_list: list[WordFilter] = list()
        print(f"Initialised with {len(self.word_list)} words")

    def add_filter(self, word_filter):
        self.filter_list.append(word_filter)

    def load_master_list(self):
        with open("resource/wordle-set.txt") as f:
        # with open("resource/sowpods-five.txt") as f:
            for line in f.readlines():
                self.word_list.append(line.strip())
        self.master_list = self.word_list
        print(f"Total word list loaded with {len(self.word_list)} words")

    def handle_selection(self, value):
        if value == "1":
            self.load_master_list()
        elif value == "2":
            filter_string = input("Enter in the format: words/bbygb\n")
            self.add_filter(self.generate_filter(filter_string))
            self.prune_filters()
            self.apply_filter()

    def prune_filters(self):
        pass

    def generate_filter(self, string_filter):
        pass

    def apply_filter(self):
        pass
