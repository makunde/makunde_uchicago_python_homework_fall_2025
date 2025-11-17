"""The greatest common divisor (GCD) of a and b is the
largest number that divides both of them with no remainder.

One way to find the GCD of two numbers is based on the
observation that if r is the remainder when a is divided
by b, then gcd(a, b) = gcd(b, r). As a base case, we can
use gcd(a, 0) = a.

Write a function that takes two whole number parameters
and and returns their greatest common divisor.
"""


def greatest_common_divisor(a, b):
    r = a % b
    print(f"r: {r}\na: {a}\nb: {b}")
    if r == 0:
        return b
    else:
        return greatest_common_divisor(b, r)


print(greatest_common_divisor(15, 20))
print(greatest_common_divisor(40, 200))
