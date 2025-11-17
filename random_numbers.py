"""
Create a module named random_numbers.
The module should contain a single function
named generate. The function should take an int
argument that specifies how many numbers to
generate in the dataset and a Bool to indicate
if the data should be saved to a file named numbers.txt.
This file should be overwritten each time the function
is run.

The function should create a data set by generating n random
numbers between 0-100. The function should return the numbers
in ascending order as a list.
"""

import random


def generate(numbers_to_generate, write_to_file):
    random_ints = sorted([random.randint(0, 100) for x in range(numbers_to_generate)])
    if write_to_file:
        with open(
            "/Users/georg/Documents/uchicago_concepts_of_programming/assignment_4/numbers.txt",
            "w",
        ) as f:
            for integer in random_ints:
                f.write(str(integer) + "\n")
    return random_ints
