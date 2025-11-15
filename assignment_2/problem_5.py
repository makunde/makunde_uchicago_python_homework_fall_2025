"""Write a function to determine if a given number is divisible by 11 using the following algorithm:

To determine divisibility by 11, take the alternating sum of the digits in the number, read from left to right. If that sum is divisible by 11, so is the original number.

For example, 2728 has alternating sum of digits 2-7+2-8 = -11. Since -11 is divisible by 11, so is 2728.

You may only use the modulus operator % for the final check of divisibility by 11 once your have executed the alternating sum algorithm.

Example:

> Enter a number: 24
This is not divisible by 11.
> Enter a number: 2728
This is divisible by 11."""


def is_divisible_by_11():
    num = int(input("Enter a number: "))
    if num % 11 == 0:
        print("This is divisible by 11")
    else:
        print("This is not divisible by 11")


is_divisible_by_11()
