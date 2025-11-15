"""Let's play Hangman!

Select a random word from the list of the most 1000 most common words and allow the user to guess it.

Here is a flow the game:"""

import random

import hangman
from hangman import Outcome


def main():
    random_index = random.randint(0, 999)
    file = open(
        "/Users/georg/Documents/uchicago_concepts_of_programming/assignment_4/common_words.txt"
    )
    random_word = file.read().splitlines()[random_index]
    game_outcome = hangman.guess_word(random_word)
    if game_outcome == Outcome.WIN:
        print(f"Congratulations!\nThe word was {random_word.upper()}.")
    if game_outcome == Outcome.LOSS:
        print(f"Sorry you lost. The word was {random_word.upper()}.")
        play_again = input("would you like to play again? (Y/N): ")
        if play_again.lower() == "y":
            main()


if __name__ == "__main__":
    main()
