from random import choice

from HangManApp.utils.utils import blank_list, all_indexes, indexes_to_value, replace


class Game:
    MAX_INCORRECT_GUESSES = 6
    LOST = 'lost'
    WON = 'won'
    RUNNING = 'running'

    def __init__(self, name: str):
        self.name = name.upper()
        self.char_list = list(self.name)
        self.word_length = len(self.char_list)
        self.show_char_list = self.init_show_char_list()
        self.incorrect_guess = 0
        self.status = self.RUNNING
        self.game_over = False
        self.chars_known = []
        for show_char in self.show_char_list:
            self.add_chars_known(show_char)

    def add_chars_known(self, char):
        if char is not ' ' and char not in self.chars_known:
            self.chars_known.append(char)

    def init_show_char_list(self):
        list1 = self.char_list
        list2 = blank_list(self.word_length)
        char1 = choice(list1)
        char = choice(list1)
        index_list = all_indexes(list1, char)
        indexes_to_value(list2, index_list, char)
        index_list = all_indexes(list1, char1)
        indexes_to_value(list2, index_list, char1)
        index_list = all_indexes(list1, ' ')
        indexes_to_value(list2, index_list, ' ')
        return list2

    def enter(self, char):
        if not self.game_over:
            if char in self.char_list:
                index_list = all_indexes(self.char_list, char)
                indexes_to_value(self.show_char_list, index_list, char)
                self.add_chars_known(char)
                self.check()
                return True
            else:
                self.incorrect_guess += 1
                self.add_chars_known(char)
                self.check()
                return False
        elif self.game_over:
            return self.status

    def check(self):
        if self.incorrect_guess > self.MAX_INCORRECT_GUESSES:
            self.status = self.LOST
            self.game_over = True
        elif self.char_list == self.show_char_list:
            self.status = self.WON
            self.game_over = True
