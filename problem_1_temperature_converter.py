"""Revisit your temperature converter and improve your code base by adding
unit tests. This may require you to refactor your code.

In your unit tests, test for any type conversion errors that may occur
from user input. Also, test that the formula you are using for the
conversion is accurate under all possible valid input. Use accuracy to
2 decimal places while testing.

Write as many tests as necessary to exhaust all possible cases (that
you can think of)."""

AFTER_INCORRECT_INPUT = "Please enter a numeric temperature: "
PROMPT = "Enter a temperature in Farenheit: "


# This implementation does not exit after the program and contiously prompts the user until they enter a valid input
def temp_converter(temp):
    # Formula for conversion https://www.calculatorsoup.com/calculators/conversions/fahrenheit-to-celsius.php
    return round((temp - 32) / (9 / 5), 2)


def validate_user_input(temp):
    f = None
    while f == None:
        try:
            f = int(temp)
        except ValueError:
            temp = input(AFTER_INCORRECT_INPUT)
    return f


def main():
    temp = input(PROMPT)
    temp = validate_user_input(temp)
    c = temp_converter(temp)
    print(f"The temperature is {c} in Celsius.")


if __name__ == "__main__":
    main()
