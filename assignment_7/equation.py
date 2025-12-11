import random
from problem_2 import Fraction
import re

OPERATORS = ["+", "-", "*", "/"]
FRACTION_REGEX = re.compile(r"^(-?[0-9]+)/(-?[0-9]+)$|^(-?[0-9]+)$")


def get_difficulty():
    difficulty = 50
    try:
        mode = int(
            input("select\n1 for easy mode\n2 for medium mode\n3 for hard mode\n> ")
        )
        if mode < 1 or mode > 3:
            raise ValueError
    except ValueError:
        print("Invalid selection falling back to medium mode")
    if mode == 1:
        return 10
    if mode == 2:
        return 50
    if mode == 3:
        return 99
    return difficulty


class Equation:
    """Attributes"""

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.first_fraction, self.second_fraction = self._generate_random_fractions()
        self.operator = random.choice(OPERATORS)
        self.correct_answer = self._solve_equation()
        self.user_provided_answer = self._get_user_answer_as_fraction()

    def _generate_random_fractions(self):
        random_denominator = random.randint(1, self.difficulty)
        random_numerator = random.randint(1, random_denominator)
        random_denominator2 = random.randint(1, self.difficulty)
        random_numerator2 = random.randint(1, random_denominator2)
        return (
            Fraction(random_numerator, random_denominator),
            Fraction(random_numerator2, random_denominator2),
        )

    def _solve_equation(self):
        if self.operator == "+":
            return self.first_fraction + self.second_fraction
        if self.operator == "-":
            return self.first_fraction - self.second_fraction
        if self.operator == "*":
            return self.first_fraction * self.second_fraction
        if self.operator == "/":
            return self.first_fraction / self.second_fraction

    def _prompt_for_answer(self):
        return input(
            f"what is {self.first_fraction} {self.operator} {self.second_fraction}? "
        )

    def _get_user_answer_as_fraction(self):
        match = FRACTION_REGEX.findall(self._prompt_for_answer())
        if not match:
            print(
                "Incorrect format! Please enter a fraction like '3/4' or a whole number like '5'. This attempt will not count."
            )
            return None

        if match[0][2]:
            numerator = int(match[0][2])
            denominator = 1
        else:
            numerator = int(match[0][0])
            denominator = int(match[0][1])
            if denominator == 0:
                print("Error: denominator cannot be zero! This attempt will not count.")
                return None

        return Fraction(numerator, denominator)

    def is_user_correct(self):
        if self.user_provided_answer is None:
            return False
        return self.correct_answer == self.user_provided_answer
