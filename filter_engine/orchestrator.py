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
        if len(string_filter) != 11:
            print("Incorrect format")
            return
        split_filter = string_filter.split('/')
        for index in range(0, 5):
            if split_filter[0][index] not in ("B", "Y", "G"):
                self.filter_list.append(
                    WordFilter(split_filter[1][index].upper(), split_filter[0][index].lower(), index))
            else:
                print("Incorrect colors given")
                break

    def apply_filter(self):
        for fil in self.filter_list:
            if not fil:
                continue
            if fil.mode == "B":
                self.apply_filter_black(fil.letter)
            elif fil.mode == "Y":
                self.apply_filter_yellow(fil.letter, fil.index)
            elif fil.mode == "G":
                self.apply_filter_green(fil.letter, fil.index)

    def apply_filter_black(self, letter):
        self.word_list = [x for x in self.word_list if letter not in x]

    def apply_filter_yellow(self, letter, index):
        temp = []
        for word in self.word_list:
            if word[index] != letter and letter in word:
                temp.append(word)
        self.word_list = temp

    def apply_filter_green(self, letter, index):
        temp = []
        for word in self.word_list:
            if word[index] == letter:
                temp.append(word)
        self.word_list = temp

