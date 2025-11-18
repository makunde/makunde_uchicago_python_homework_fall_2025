"""Now that we are becoming better Scrabble players, construct a program that will help us identify the highest scoring
words from our rack of tiles.

Write a program that prompts the user to enter the tiles in their rack as below:

> Enter the each letter in your rack:
t r a b w q f
Your program should validate the inputed data and prompt the user if they enter a bad character (eg. a number).

Also, note that a rack contains at most seven tiles.

You should be able to handle input entered in any of the following formats:

trabwqf
t r a b w q f
t,r,a,b,w,q,f
Use regular expression to test which input format the user has entered. You may use any approach to separate the characters.

Once you have isolated the letters, identify every word combination of any length that can be made from the letters. Use the
itertools. package to assist in identifying the combinations and permutations of the letters. Use
the list of allowed Scrabble words, scrabble_list.txt, to verify if the letter combinations you have created represents a
valid word.

Present a list to the user of the 15 highest scoring words for each word length from the available letters. The output
should be sorted in descending order. If there are no possible words of a given length, report "no words". Follow the
example given below:

> Enter the each letter in your rack:
t r a b w q 3
3 is not a valid letter. Please try again.


> Enter the letters in your rack?
trabwqe


2 Letter Words
--------------
aa - 2 points
no - 2 points
...
...


3 Letter Words
--------------
bat - 6 points
rat - 7 points
...
...


4 Letter Words
--------------
bare - 4 points
...


5 Letter Words
--------------
water - 7 points
...
...


6 Letter Words
--------------
no words


7 Letter Words
--------------
no words

This program should make use of best practices in code design and modularization. The program should be able to be run from the command line and utilize a main() function that drives the entire program.

Specific functionality should be factored out into dedicated functions and related functions should be collected into modules."""

import os
import scrabble

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
SCRABBLE_WORDS_FILE = CURRENT_DIRECTORY + "/scrabble_list.txt"


def main():
    rack_letters = input("Enter the each letter in your rack: ")
    is_valid_scrable_rack = scrabble.validate_scrable_rack(rack_letters)
    if not is_valid_scrable_rack:
        return
    all_possible_letter_combos = scrabble.get_all_possible_letter_combos(rack_letters)
    all_possible_scrable_words = scrabble.load_valid_scrable_words(SCRABBLE_WORDS_FILE)
    valid_words = scrabble.get_sorted_valid_words_from_letter_combos(
        all_possible_letter_combos, all_possible_scrable_words
    )
    top_15_words_per_length = scrabble.save_top_15_words_for_each_length(valid_words)
    scrabble.display_top_words_for_each_length(top_15_words_per_length)


if __name__ == "__main__":
    main()
