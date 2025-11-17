"""
words.py Module for Scrabble scoring
"""
import re


def points_for_letter(letter):
    """Return the points as an integer for a given letter according to Scrabble
    letter frequency tables.
    """  
    
    # Dictionary to look up the point value for each letter. In the dictionary,
    # the key is the letter and the value is the point value
    tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                 "x": 8, "z": 10}
    return tile_score[letter]

def get_scores_from_file(filename):
    text = open(filename).read()
    word_pattern = re.compile(r"(?:^|\n)([a-zA-Z]{3})\b")
    words_list = word_pattern.findall(text)
    print(words_list)
    scores = []
    for word in words_list:
        score = 0
        for char in word:
            score += points_for_letter(char.lower())
        scores.append((word, score))
    return scores

def sort_scores(scores):
    return sorted(scores, key=lambda x: x[1])

def write_scores_to_file(scores, filename):
    with open(filename, "w") as f:
        for score in scores:
            score_text = f"{score[0]} -> {score[1]}\n"
            f.write(score_text)
    
