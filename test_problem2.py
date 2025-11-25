import pytest
from problem_2 import Fraction

"""Unit tests for the Fraction class. 

   You do not need to use this to complete the assignment,
   it is for your own testing and debugging. If your class
   is implemented correctly, it should pass all the tests.
"""


def test_initialization():
    """Test fraction creation"""
    f = Fraction(5, 8)
    assert f.__str__() == "5/8"
    assert f.as_decimal == 0.625


def test_throws_when_denominator_is_zero():
    with pytest.raises(ValueError):
        assert Fraction(5, 0)


def test_add():
    """Test the addition function"""
    f1 = Fraction(5, 8)
    f2 = Fraction(5, 8)

    add_them_up = f1 + f2
    assert add_them_up.__str__() != "10/8"
    assert add_them_up.__str__() != "5/4"
    assert add_them_up.__str__() == "1-1/4"
    assert add_them_up.as_decimal == 1.25


def test_subtract():
    """Test the addition function"""
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 1)

    total = f1 / f2
    assert total.__str__() == "1/4"
    assert total.as_decimal == 0.25


def test_multiply():
    """ """
    f1 = Fraction(5, 8)
    f2 = Fraction(2, 1)
    f3 = f1 * f2
    assert f3.__str__() != "10/8"
    assert f3.as_decimal == 1.25


def test_divide():
    """ """
    f1 = Fraction(5, 8)
    f2 = Fraction(1, 1)
    f3 = f1 / f2
    assert f3.__str__() == "5/8"
    assert f3.as_decimal == 0.625


def test_eq():
    """ """
    f1 = Fraction(5, 8)
    f2 = Fraction(5, 8)
    f3 = Fraction(1, 2)

    assert f1 == f2
    assert f1 != f3
