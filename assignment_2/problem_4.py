"""Implement a function that takes three numbers as input and returns the largest of the three. While there is a built-in function max() in Python, do not use it.

Do take a minute to look up this function (help(max)) and see how you might use it in the future.

# Complete this function to find and return the largest of three numbers"""


def max_of_three(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


print(max_of_three(20, 3, 22))
print(max_of_three(25, 3, 22))
print(max_of_three(20, 28, 22))
print(max_of_three(-20, -3, -22))
