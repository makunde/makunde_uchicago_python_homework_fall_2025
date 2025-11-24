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


class Word:
    """Represents a single Scrabble word with its score and length.
    
    Attributes:
        chars: The word characters
        score: Scrabble score for this word
        length: Number of characters in the word
    """

    def __init__(self, chars, score):
        """Initialize a Word with characters and score.
        
        Args:
            chars: The word as a string
            score: The calculated Scrabble score
        """
        self.chars = chars
        self.score = score
        self.length = self._get_length()

    def __str__(self):
        """Return string representation of word with score."""
        return f"{self.chars} - {self.score} points"

    def __lt__(self, other):
        """Compare words by length, then score, then alphabetically."""
        if self.length != other.length:
            return self.length < other.length
        if self.score != other.score:
            return self.score < other.score
        return self.chars < other.chars

    def __gt__(self, other):
        """Compare words by length, then score, then alphabetically."""
        if self.length != other.length:
            return self.length > other.length
        if self.score != other.score:
            return self.score > other.score
        return self.chars > other.chars

    def __le__(self, other):
        """Compare words by length, then score, then alphabetically."""
        if self.length != other.length:
            return self.length <= other.length
        if self.score != other.score:
            return self.score <= other.score
        return self.chars <= other.chars
    
    def __ge__(self, other):
        """Compare words by length, then score, then alphabetically."""
        if self.length != other.length:
            return self.length >= other.length
        if self.score != other.score:
            return self.score >= other.score
        return self.chars >= other.chars
    
    def __eq__(self, other):
        """Check if two words are equal (same chars, score, and length)."""
        score_match = self.score == other.score
        length_match = self.length == other.length
        char_match = self.chars == other.chars
        return score_match and length_match and char_match
    
    def __ne__(self, other):
        """Check if two words are not equal."""
        score_match = self.score == other.score
        length_match = self.length == other.length
        char_match = self.chars == other.chars
        return not (score_match and length_match and char_match)

    def _get_length(self):
        """Calculate and return the length of the word."""
        return len(self.chars)


class ScrabbleInputValidator:
    """Validates and processes user input for Scrabble rack letters.
    
    Attributes:
        _raw_rack_letters: User input for scrabble rack (private)
        valid_rack_letters: Cleaned letters (no spaces/commas) or None if invalid
    """
    def __init__(self, rack_letters):
        """Initialize validator with raw input.
        
        Args:
            rack_letters: User input string for Scrabble rack
        """
        self._raw_rack_letters = rack_letters
        self.valid_rack_letters = self._get_valid_rack_letters()

    def _is_valid_scrable_rack(self):
        """Check if input matches valid format (1-7 letters with optional spaces/commas).
        
        Returns:
            True if valid format, False otherwise. Prints error message if invalid.
        """
        if not LETTER_FORMAT_PATTERN.match(self._raw_rack_letters):
            print(
                "Letters must be in valid format with 7 letters max. Examples: trabwqf | t r a b w q f | t,r,a,b,w,q,f"
            )
            return False
        return True
    
    def _get_valid_rack_letters(self):
        """Extract and return valid letters from input, or None if invalid.
        
        Returns:
            List of cleaned letters (lowercase) if valid, None if invalid
        """
        if self._is_valid_scrable_rack():
            return LETTER_EXTRACTOR_PATTERN.findall(self._raw_rack_letters.lower())
        return None

    
    


class ScrabbleWordValidator:
    """Validates and generates valid Scrabble words from a rack of letters.
    
    This class takes a Scrabble rack of letters and finds all valid words that can be
    made from those letters by comparing against a dictionary file. Words are sorted
    by length (descending), then by score (descending).
    
    Attributes:
        _filename: Path to the Scrabble dictionary file (private)
        _scrable_rack: List of letters from the input rack (private)
        _valid_words_set: Set of all valid words from the dictionary file (private)
        _all_letter_permutations: All possible letter permutations from the rack (private)
        valid_scrable_words_from_input: List of valid Word objects sorted by length and score
    """

    def __init__(self, filename, scrable_rack):
        """Initialize the validator with a dictionary file and rack of letters.
        
        Args:
            filename: Path to the Scrabble dictionary file
            scrable_rack: List of letters available in the rack
        """
        self._filename = filename
        self._scrable_rack = scrable_rack
        self._valid_words_set = self._load_valid_scrable_words()
        self._all_letter_permutations = self._get_all_possible_letter_combos()
        self.valid_scrable_words_from_input = self._get_sorted_valid_words_from_letter_combos()

    def _load_valid_scrable_words(self):
        """Load all valid words from the dictionary file into a set.
        
        Returns:
            Set of valid Scrabble words (uppercase) from the dictionary file
        """
        return set(open(self._filename).read().splitlines())

    def _get_all_possible_letter_combos(self):
        """Generate all possible permutations of the rack letters (1 to 7 letters).
        
        Returns:
            List of strings representing all permutations of the rack letters
        """
        all_possible_permutations = []
        for i in range(1, len(self._scrable_rack)):
            length_of_possible_words = i + 1
            all_possible_permutations += itertools.permutations(
                self._scrable_rack, length_of_possible_words
            )
        return ["".join(char) for char in all_possible_permutations]

    def _get_sorted_valid_words_from_letter_combos(self):
        """Find all valid words from permutations that exist in the dictionary.
        
        Checks each permutation against the valid words set, calculates the Scrabble
        score, creates Word objects, and sorts them by length and score (descending).
        
        Returns:
            List of Word objects sorted by length (desc), then score (desc)
        """
        validated = []
        for permutation in self._all_letter_permutations:
            if permutation.upper() not in self._valid_words_set:
                continue
            score = 0
            for char in permutation:
                score += TILE_SCORE[char]
            validated.append(Word(permutation, score))
        return sorted(validated, reverse=True)


class WordDisplayer:
    """Displays top Scrabble words organized by word length.
    
    Takes a list of valid words and organizes them by length, keeping at most the top 15
    words for each length. Displays the organized words to console.
    
    Attributes:
        _top_15_words_for_each_length_dict: Dictionary mapping word length to top words up to 15 (private)
    """
    
    def __init__(self, words):
        """Initialize the displayer with a list of words.
        
        Args:
            words: List of Word objects to organize and display
        """
        self._top_15_words_for_each_length_dict = self._save_top_15_words_for_each_length(words)

    def _save_top_15_words_for_each_length(self, words_list):
        """Organize words by length and keep top words up to 15 for each length.
        
        Args:
            words_list: List of Word objects to organize
            
        Returns:
            Dictionary mapping word length (int) to list of up to 15 Word objects
        """
        word_count = 0
        save_words_for_length = {}
        current_length = -1
        for word in words_list:
            if word.length != current_length:
                current_length = word.length
                word_count = 0
            if word_count == 15:
                word_count = 0
                continue
            word_count += 1
            save_words_for_length[word.length] = save_words_for_length.get(
                word.length, []
            ) + [word]
        return save_words_for_length

    def display_top_words_for_each_length(self):
        """Display up to 15 of the top words for each word length to console.
        
        Prints words grouped by length in descending order of score.
        Format: "N Letter Words" followed by top 15 words as "word - score points"
        """
        for length, words in self._top_15_words_for_each_length_dict.items():
            print(f"\n{length} Letter Words\n--------------")
            words.reverse()
            for word in words:
                print(word)