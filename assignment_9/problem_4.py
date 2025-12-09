"""
The following function accepts a list of
numbers and computes the product of all the odd numbers.

def product_of_odds(list):
  result = 1
  for i in list:
    if i % 2 == 1:
      result *= i
  return result
Rewrite the function using a combination of
lambda, map, reduce and filter.

Use the following template and provide your
code for reduce_function, filter_function,
and map_function.
"""

from functools import reduce

reduce_function = lambda x, y: x * y
filter_function = lambda x: x % 2 == 1
map_function = lambda x: x

def product_of_odds(list):
    return reduce(reduce_function, \
      filter(filter_function, \
        map(map_function, list)), 1)

if __name__ == "__main__":
    print("should be 15:", product_of_odds([1, 2, 3, 4, 5]))
    print("should be 1:", product_of_odds([2, 4, 6, 8]))