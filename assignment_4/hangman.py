from enum import Enum

TOTAL_GUESSES = 5
SPACE = " "
PERIOD = "."
PLACE_HOLDER = "_"

class Outcome(Enum):
    WIN = 1
    LOSS = 2

def guess_word(word):
    letters_in_word = {x: False for x in word}
    for i in range(TOTAL_GUESSES):
        if i > 0:
            print(f"You have {TOTAL_GUESSES-i} guesses remaining")
        guess = input("guess a letter: ")
        if guess in letters_in_word:
            letters_in_word[guess] = True
            progress = show_progress(word, guess)
            if all(letters_in_word.values()):
                return Outcome.WIN
            print(f"{guess} is in the word {progress}")
            guess = input("try and guess the word: ")
            if guess == word:
                return Outcome.WIN
            print("That is not the word")
        else:
            print(f"{guess} is not in the word")
    return Outcome.LOSS


def show_progress(word, guess):
    progress = ""
    for i in range(len(word)):
        if word[i] == guess:
            progress += word[i]
        else:
            progress += PLACE_HOLDER
        if i == len(word):
            progress += PERIOD
        else:
            progress+=SPACE
    return progress