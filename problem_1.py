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
    valid_scrable_rack = ScrabbleInputValidator(rack_letters).valid_rack_letters
    if valid_scrable_rack == None:
        return
    valid_scrable_rack = ScrabbleWordValidator(
        SCRABBLE_WORDS_FILE, valid_scrable_rack
    ).valid_scrable_words_from_input
    WordDisplayer(valid_scrable_rack).display_top_words_for_each_length()


if __name__ == "__main__":
    main()
