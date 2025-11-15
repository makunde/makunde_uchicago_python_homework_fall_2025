"""Create a temperature converter program that takes input from a user in Fahrenheit and converts it to Celsius.
You should check that the input is valid (ie. the input is a positive, whole number). If it is not, warn the user to enter a whole number,
positive number and exit the program.  If it is a valid number, print the temperature rounded to two decimal places.

The program should behave similar to the example below:

Example:

> Enter a temperature in Fahrenheit: 32
The temperature is 0.00 in Celsius.

> Enter a temperature in Fahrenheit: 100
The temperature is 37.78 in Celsius.
In the case where the input is invalid:

> Enter a temperature in Fahrenheit: 32.5
Please enter a positive, whole number numeric temperature.
> Enter a temperature in Fahrenheit: thirty two
Please enter a positive, whole number numeric temperature."""

AFTER_INCORRECT_INPUT = "Please enter a positive, whole number numeric temperature: "


# This implementation does not exit after the program and contiously prompts the user until they enter a valid input
def temp_converter():
    f = None
    prompt = "Enter a temperature in Farenheit: "
    while f == None:
        try:
            f = int(input(prompt))
            if f < 0:
                f = None
                prompt = AFTER_INCORRECT_INPUT
        except ValueError:
            prompt = AFTER_INCORRECT_INPUT

    # Formula for conversion https://www.calculatorsoup.com/calculators/conversions/fahrenheit-to-celsius.php
    c = round((f - 32) / (9 / 5), 2)
    print(f"The temperature is {c} in Celsius.")


temp_converter()
