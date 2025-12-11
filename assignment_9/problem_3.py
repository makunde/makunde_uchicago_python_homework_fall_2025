"""
Write a function that determines the maximum
value from a list of numerical values.

def max_number(list_of_numbers):
  pass
Write a statement using reduce that also
determines the maximum value of a list of
numerical values.

reduce(something,something)
Compare the two approaches in terms of the
time complexity. You may want to sneek a peek
at the implementation of any of the Python
standard library functions you are using.
"""

from functools import reduce


def max_number(list_of_numbers):
    if not list_of_numbers:
        return None

    max_val = list_of_numbers[0]
    for num in list_of_numbers[1:]:
        if num > max_val:
            max_val = num

    return max_val


max_with_reduce = lambda lst: reduce(lambda a, b: a if a > b else b, lst)

"""
APPROACH 1: Manual iteration (max_number function)
- Time Complexity: O(n) - iterates through list once
- Space Complexity: O(1) - only stores current maximum
- Implementation: Simple loop with comparison

APPROACH 2: Using reduce
- Time Complexity: O(n) - reduce still visits each element
- Space Complexity: O(n) - Python's reduce can use call stack
- Implementation: Functional approach using lambda

EFFICIENCY NOTES:
The built-in max() function in Python is implemented in C and is highly optimized,
making it faster than both custom implementations for large datasets. However, the
time complexity of all three approaches is O(n), meaning they scale linearly with
the size of the input list. The main differences are in constant factors and 
implementation overhead, not algorithmic complexity.
"""

if __name__ == "__main__":
    test_list = [3, 7, 2, 9, 1, 5]

    print(f"Manual function: {max_number(test_list)}")
    print(f"Using reduce: {max_with_reduce(test_list)}")
    print(f"Built-in max: {max(test_list)}")
