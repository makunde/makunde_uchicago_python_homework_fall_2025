"""
Now that you have learned about the benefits of object oriented programming,
go back and redo Problem 2 (Scrabble word generator) from last week in an
object oriented programming style. You should be able to reuse almost all
of your code as-is; this is more an exercise in refactoring and software
design.

Define classes that perform specific responsibilities in your program.
Include a class named Word that stores each word, its length and score.
"""

import os
from scrabble import ScrabbleInputValidator
from scrabble import ScrabbleWordValidator
from scrabble import WordDisplayer

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
SCRABBLE_WORDS_FILE = CURRENT_DIRECTORY + "/scrabble_list.txt"


def main():
    rack_letters = input("Enter the each letter in your rack: ")
    scrable_input = ScrabbleInputValidator(rack_letters)
    if scrable_input.valid_rack_letters is None:
        return
    scrable_words = ScrabbleWordValidator(
        SCRABBLE_WORDS_FILE, scrable_input.valid_rack_letters
    )
    WordDisplayer(
        scrable_words.valid_scrable_words_from_input
    ).display_top_words_for_each_length()


if __name__ == "__main__":
    main()
