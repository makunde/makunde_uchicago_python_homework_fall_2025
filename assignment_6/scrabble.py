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


def display_letters_for_slack(desired_letters):
    final_string = ""
    for char in desired_letters:
        if char == " ":
            char = "blank"
        if char in PUNCTUATION:
            final_string += char
            continue
        final_string += f":scrabble-{char.lower()}:"
    print(final_string)
