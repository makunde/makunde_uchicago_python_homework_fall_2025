"""
Write a program that allows a user to practice fraction operations.
The program should present a randomly selected operation (i.e. addition,
multiplication, division, subtraction) and a pair of randomly generated
fractions.

The program should keep track of the number of completed and attempted
problems and report them at the end.

Running the program should look similar to the following:"""

from equation import get_difficulty
from equation import Equation

""" """


def main():
    print("Welcome to Action Fractions!")
    difficulty = get_difficulty()
    continue_solving = "y"
    correct = 0
    attempts = 0
    while continue_solving == "y":
        attempts += 1
        equation = Equation(difficulty)
        if equation.user_provided_answer is None:
            attempts -= 1
            continue
        if equation.is_user_correct():
            correct += 1
            print("Corect!")
        else:
            print("Incorrect!")
        continue_solving = input("Would you like another problem [y/n]? ").lower()

    print(
        f"You answered {correct}/{attempts} problems correctly. Keep up the good work!"
    )


if __name__ == "__main__":
    main()
