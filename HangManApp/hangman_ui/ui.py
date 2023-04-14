from string import ascii_uppercase
from os import system

from HangManApp.hangman_game.game import Game


class UI:
    HANGMAN_STAGES = [
        '''
        +---+
            |
            |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
            |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
         \\  |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
        '''
    ]

    @classmethod
    def show_hangman(cls, stage: int):
        return cls.HANGMAN_STAGES[stage]

    def __init__(self, game: Game, name: str):
        self.game = game
        self.name = name

    def title(self):
        system('cls')
        print(f'********** {self.name} Hangman Game **********\n\n')
        self.display_show_hangman()
        print('characters entered or known: ', end="")
        for char in self.game.chars_known:
            print(char, ' ', end="")
        print('\n\n')
        for char in self.game.show_char_list:
            if char == ' ':
                print('     ⎵', end="")
            print('     \x1B[4m', char, "\x1B[0m", end="")
        print('\n\n')

    def display_show_hangman(self):
        print('     ', self.show_hangman(self.game.incorrect_guess))

    def game_run(self):
        while not self.game.game_over:
            self.title()
            print('      chances left: ', self.game.MAX_INCORRECT_GUESSES - self.game.incorrect_guess + 1, '\n\n')
            self.enter()
        if self.game.status == Game.WON:
            self.title()
            print('      chances left: ', self.game.MAX_INCORRECT_GUESSES - self.game.incorrect_guess, '\n\n')
            self.won(self.game.name)
        elif self.game.status == Game.LOST:
            self.title()
            self.lost(self.game.name)

    def enter(self):
        char_input = input("     Enter a character: ")
        char_input = char_input.upper()
        if char_input == '' or char_input[0] not in ascii_uppercase:
            print("\nEnter a valid character")
            self.enter()
        elif char_input[0] in self.game.chars_known:
            print("\nEnter a new character")
            self.enter()
        else:
            char_input = char_input[0]
            self.game.enter(char_input)

    @staticmethod
    def won(word: str):
        print("     You have won the game! ")
        print('You guessed the word right! : ', word)
        __ = input()

    @staticmethod
    def lost(word: str):
        print("     You have lost the game! \n\n")
        word = word.upper()
        print('The word was: ', word)
        __ = input()
