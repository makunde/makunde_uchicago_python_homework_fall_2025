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
import re
import itertools

TILE_SCORE = {
    "a": 1,
    "c": 3,
    "b": 3,
    "e": 1,
    "d": 2,
    "g": 2,
    "f": 4,
    "i": 1,
    "h": 4,
    "k": 5,
    "j": 8,
    "m": 3,
    "l": 1,
    "o": 1,
    "n": 1,
    "q": 10,
    "p": 3,
    "s": 1,
    "r": 1,
    "u": 1,
    "t": 1,
    "w": 4,
    "v": 4,
    "y": 4,
    "x": 8,
    "z": 10,
}
LETTER_FORMAT_PATTERN = re.compile(r"^(?:[a-zA-z][\s,]?){1,7}$")
LETTER_EXTRACTOR_PATTERN = re.compile(r"[a-zA-Z]")
PUNCTUATION = ".!?"

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
SCRABBLE_WORDS_FILE = CURRENT_DIRECTORY + "/scrabble_list.txt"


class Word:   
 """Attributes:    
          - characters   
          - length - score  
     """   
 # Your code here   
 pass

class InputValidator:   
 pass   

class WordValidator:   
 pass   

class WordGenerator:   
 pass   

def validate_scrable_rack(rack_letters):
    if not LETTER_FORMAT_PATTERN.match(rack_letters):
        print(
            "Letters must be in valid format with 7 letters max. Examples: trabwqf | t r a b w q f | t,r,a,b,w,q,f"
        )
        return False
    return True


def get_all_possible_letter_combos(rack_letters):
    rack_letters = LETTER_EXTRACTOR_PATTERN.findall(rack_letters.lower())
    all_possible_permutations = []
    for i in range(1, len(rack_letters)):
        length_of_possible_words = i + 1
        all_possible_permutations += itertools.permutations(
            rack_letters, length_of_possible_words
        )
    return ["".join(char) for char in all_possible_permutations]


def load_valid_scrable_words(filename):
    return set(open(filename).read().splitlines())


def get_sorted_valid_words_from_letter_combos(letter_combos, valid_words_set):
    validated = []
    for permutation in letter_combos:
        if permutation.upper() not in valid_words_set:
            continue
        score = 0
        for char in permutation:
            score += TILE_SCORE[char]
        validated.append((len(permutation), score, permutation))
    return sorted(validated, reverse=True)


def save_top_15_words_for_each_length(words_data_list):
    word_count = 0
    save_words_for_length = {}
    current_length = -1
    for length, score, word in words_data_list:
        if length != current_length:
            current_length = length
            word_count = 0
        if word_count == 15:
            word_count = 0
            continue
        word_count += 1
        result_string = f"{word} - {score} points"
        save_words_for_length[length] = save_words_for_length.get(length, []) + [
            result_string
        ]
    return save_words_for_length


def display_top_words_for_each_length(top_words_per_length):
    for length, words in top_words_per_length.items():
        print(f"\n{length} Letter Words\n--------------")
        words.reverse()
        for word_score_string in words:
            print(word_score_string)


def main():
    rack_letters = input("Enter the each letter in your rack: ")
    is_valid_scrable_rack = validate_scrable_rack(rack_letters)
    if not is_valid_scrable_rack:
        return
    all_possible_letter_combos = get_all_possible_letter_combos(rack_letters)
    all_possible_scrable_words = load_valid_scrable_words(SCRABBLE_WORDS_FILE)
    valid_words = get_sorted_valid_words_from_letter_combos(
        all_possible_letter_combos, all_possible_scrable_words
    )
    top_15_words_per_length = save_top_15_words_for_each_length(valid_words)
    display_top_words_for_each_length(top_15_words_per_length)


if __name__ == "__main__":
    main()