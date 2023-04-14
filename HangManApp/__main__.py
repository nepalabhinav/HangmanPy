from HangManApp.hangman_game.game import Game

from HangManApp.hangman_ui.ui import UI

from HangManApp.utils.utils import random_country


def main():
    while True:
        choice = input(
            "Welcome To my Hangman game of random countries\nDon't type or type any character and press ENTER to enter "
            "the game\nType 'exit' and press ENTER to exit the game")
        if choice == 'exit':
            exit()
        else:
            game = Game(random_country())
            UI(game, 'Abhinav Nepal Country names').game_run()


if __name__ == '__main__':
    main()
