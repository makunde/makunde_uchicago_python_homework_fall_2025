"""
We now have custom Scrabble emojis in Slack!

To insert a scrabble emoji, follow the format :scrabble-X: where X is the letter you want.
If you want a blank tile, type :scrabble-blank:.

Write a small utility program that prompts the user for text, converts it to Scrabble emoji
format and prints it to the command line.

For example:

% python scrabble_emoji.py
> emoji
:scrabble-e::scrabble-m::scrabble-o::scrabble-j::scrabble-i:
Keep any punctuation as is.

% python scrabble_emoji.py

>I went to grad school for this?

:scrabble-i::scrabble-blank::scrabble-w::scrabble-e::scrabble-n::scrabble-t::scrabble-blank::scrabble-t::scrabble-o::scrabble-blank::scrabble-g::scrabble-r::scrabble-a::scrabble-d::scrabble-blank::scrabble-s::scrabble-c::scrabble-h::scrabble-o::scrabble-o::scrabble-l::scrabble-blank::scrabble-f::scrabble-o::scrabble-r::scrabble-blank::scrabble-t::scrabble-h::scrabble-i::scrabble-s:?
Now you can cut and paste the output in to Slack. The only difficult part is to show restraint on when to use it.

Please post a new word you learned from our Scrabble list in Slack module-6. Please include the definition.
"""

import re
import scrabble

VALID_SENTENCE_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z\s]*[\?.!]?")


def main():
    desired_letters = input("enter letters you want to scrabble-fy: ")
    if not VALID_SENTENCE_PATTERN.match(desired_letters):
        print(
            "enter a valid sentence. No numbers, apostrophes in a contraction or special characters. You can end with punctiation if you'd like"
        )
        return
    scrabble.display_letters_for_slack(desired_letters)


if __name__ == "__main__":
    main()
