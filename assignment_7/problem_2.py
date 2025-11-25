"""Construct a class to implement the abstract data type Fraction.
The Fraction class should have at two attributes, numerator and
denominator, that are represented by integers.

To create an instance of a Fraction override the initialization function,
init(), to take two arguments representing the numerator and the denominator.
You should ensure that the values to the initializer function are valid for a fraction:

The numerator and denominator are limited to positive and negative whole number integers.
The denominator cannot be zero.
Creating the fraction 5/8 would be made using a call such as the following:
# Create the fracion 5/8
fraction = Fraction(5,8)

The operations for the Fraction class will allow it object to behave like any other
numerical value using standard mathematical operators. Accomplish this by overriding
the mathematical operators (+,-,/,*) to allow your Fraction class to add, subtract,
multiply, and divide fractions.

For example:
f1 = Fraction(5,8)
f2 = Fraction(2,8)

# add
add_them_up = f1 + f2
print(add_them_up) # 7/8

# subtract
add_them_up = f1 - f2
print(add_them_up) # 3/8

In addition, implement the greater than (>), less than (<), and equal (==) than comparison
operators.

f1 = Fraction(5,8)
f2 = Fraction(2,8)

greater_than = f1 > f2
print(greater_than)    # True

Override the object __str__ method to print out the fraction in slash form (eg. 3/5).
Fractions should always print the result of any operation in the lowest terms as a proper
(ie. the numerator is less than the denominator) or as mixed fraction.

fraction = Fraction(5,8)
print(fraction)        # prints out 5/8

f1 = Fraction(5,8)
f2 = Fraction(5,8)
add_them_up = f1 + f2
print(add_them_up)     # prints out a mixed fraction 1-1/4
Code Resuse Note: You have previously written a function to find the greatest common denominator between two numbers.

Finally, write a method to be able to represent the value of a fraction in decimal form. Precision to 3 decimal places is sufficient.
"""


class Fraction:
    """Attributes
    numerator:
    denominator:
    """

    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.as_decimal = self._to_decimal()

    def __add__(self, other):
        self_lcm, other_lcm = self._equalize_denominators(other)
        final_numerator = self_lcm.numerator + other_lcm.numerator
        return Fraction(final_numerator, self_lcm.denominator).simplify()

    def __sub__(self, other):
        self_lcm, other_lcm = self._equalize_denominators(other)
        final_numerator = self_lcm.numerator - other_lcm.numerator
        return Fraction(final_numerator, self_lcm.denominator).simplify()

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator).simplify()

    def __div__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator).simplify()

    def __str__(self):
        self.simplify()
        wholes = 0
        leftover = self.numerator
        if self.numerator >= self.denominator:
            while leftover > self.denominator:
                wholes += 1
                leftover -= self.denominator
        if wholes > 0:
            if leftover == 0:
                return f"{wholes}"
            return f"{wholes}-{leftover}/{self.denominator}"
        return f"{self.numerator}/{self.denominator}"

    def __gt__(self, other):
        return self._to_decimal(False) > other._to_decimal(False)

    def __lt__(self, other):
        return self._to_decimal(False) < other._to_decimal(False)

    def __eq__(self, other):
        return self._to_decimal(False) == other._to_decimal(False)

    def _equalize_denominators(self, other):
        denominator = self._least_common_multiple(other)
        self_multiplication_factor = int(denominator / self.denominator)
        other_multiplication_factor = int(denominator / other.denominator)
        self_new_numerator = self.numerator * self_multiplication_factor
        other_new_numerator = other.numerator * other_multiplication_factor
        return (
            Fraction(self_new_numerator, denominator),
            Fraction(other_new_numerator, denominator),
        )

    def simplify(self):
        gcd = self._greatest_common_divisor(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)
        return self

    def _least_common_multiple(self, other):
        return int(
            abs(other.denominator * self.denominator)
            / self._greatest_common_divisor(self.denominator, other.denominator)
        )

    def _greatest_common_divisor(self, a, b):
        r = a % b
        if r == 0:
            return b
        return self._greatest_common_divisor(b, r)

    def _to_decimal(self, roundTo3=True):
        """Return a fraction object instance as a decimal rounded to 3 places"""
        if roundTo3:
            return round(self.numerator / self.denominator, 3)
        return self.numerator / self.denominator
