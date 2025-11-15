"""Write a program to prompt for a whole number score between 0 and 100 and return a corresponding letter grade.

Make sure that you check that the input is valid (ie. the input is a number). If the score is out of range, print an error
message to the user. If the score is between 0 and 100, convert the score to a grade using the following table:

A >= 90
B >= 80
C >= 70
D >= 60
F < 60
Print out the grade.

Example:

> Enter a score: 90
You received an A!
> Enter a score: 76
You received a C!
> Enter a score: fifty-six
That is not valid input.
> Enter a score: 89.9
That is not valid input.
> Enter a score: -100
That is not valid input."""

INVALID_INPUT = "that is not a valid input"


def letter_grade():
    score = None
    try:
        score = int(input("enter a score: "))
    except ValueError:
        print(INVALID_INPUT)
        return
    if score < 0:
        print(INVALID_INPUT)
        return

    if score >= 90:
        print("You received an A!")
    elif score >= 80:
        print("You received a B!")
    elif score >= 70:
        print("You received a C!")
    elif score >= 60:
        print("You received a D.")
    elif score < 60:
        print("You received a F.")


letter_grade()
