"""Create a password strength validator that prompts the user to enter a password. 
Evaluate the password using the following criteria and report back to the user if they have chosen a strong password.

The password needs to satisfy the following conditions to be strong.

Have at least 12 characters
Contains both numbers and letters
Contains at least one of the following characters: !,@,#,$,%
Contains at least one capital letter and one lower-case letter
Example:

> Enter a password: password   
This is not a strong password :(   
> Enter a password: ABC123def456!   
This is a strong password :)"""

SPECIAL_CHARACTERS = "!@#$%"
NUMBERS = "0123456789"
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"


def validate_strength():
    password = input("Enter a password: ")
    if is_strong(password):
        print("This is a strong password :)")
    else:
        print("This is not a strong password :(")

def is_strong(password):
    if len(password) < 12:
        return False
    has_special_character = False
    has_number = False 
    has_upper_case_letter = False
    has_lower_case_letter = False
    for char in password:
        if char in SPECIAL_CHARACTERS:
            has_special_character = True
        elif char in NUMBERS:
            has_number = True
        elif char in UPPER_CASE_LETTERS:
            has_upper_case_letter = True
        elif char in LOWER_CASE_LETTERS:
            has_lower_case_letter = True
    return has_lower_case_letter and has_upper_case_letter and has_number and has_special_character

validate_strength()