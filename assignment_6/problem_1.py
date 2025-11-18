"""
Question 3

In Scrabble, the score of a word is the calculated by summing the point value of each individual letter.
The point value of each letter is assigned based on the frequency of the letters in the game. Common letters
in English words have a lower score, (eg. c=3, a=1, t=1). Less common letters have a higher point value
(eg. z=10, q=10, x=8)


The following are examples of words and their score:
  `cat` has a point value of 5 where c=3 + a=1 + t=1
  `tax` has a point value of 10, where t=1 + a=1 + x=8

One of the best ways to improve as a Scrabble player is to memorize all the 2 and 3 letter words allowed
during game play.  It should be noted that many of the world's best Scrabble players consider it is a
waste of time (and brain power) to memorize the definitions of these words.

Write a program, using best practices in Python, that calculates the score for legal 3 letter words,
sorts them by score, and writes the words to a file.

Include the score when writing the words to the file, so you know which words are the most valuable
to start memorizing. Just like the professional Scrabble players, you do not need to concern yourself
with learning the definitions, so there is no need to write them to the file.

A list of all the legal 3 letter Scrabble words are provided in the `3_letter_words.txt` file. The file
is in the following format, where the word and definition are separated by a pipe character (" | ").


  AAH | to exclaim in delight
  AAL | East Indian shrub
  AAS | [aa] (rough, cindery lava)


When the program runs, it should complete the following tasks:
 - Read and parse the list of 3 letter Scrabble words from the included file
 - Compute the score for each word
 - Sort the words by descending score (ie. highest scoring words to lowest scoring words).
   If words have the same score, sort the words alphanumerically. For example `car` should be
   listed before `cat` with the same score of 5.
 - Write the words out to a file named `3_letter_words_sorted.txt`. Format your file following this example:

     zzz -> 30
     zuz -> 21
     ...
     ...
     ...
     ute -> 3
     uts -> 3


Organize your code using a module named `words` that will handle all the functions related to reading,
scoring, sorting, and writing to a file. The module has been started in the repository as `words.py` and
includes a function `points_for_letter()` to return the points for a given letter. Use a `main()` function
as the driver for your program as written below:
"""

import words
import sys
import os


def main():
    """Main driver for your program"""
    args = sys.argv[1:]
    if len(args) > 1:
        sys.stderr.write("This program takes in 1 text file max")
        sys.exit()
    scores = words.get_scores_from_file(args[0])
    scores = words.sort_scores(scores)
    current_directory = os.path.dirname(os.path.realpath(__file__))
    words.write_scores_to_file(scores, current_directory + "/3_letter_words_sorted.txt")


if __name__ == "__main__":
    main()
