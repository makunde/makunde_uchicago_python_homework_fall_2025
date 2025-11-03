"""Compute the mean, median, mode, variance and standard deviation for a
dataset of numbers. Print the computed statistical values with appropriate
labels to the console.

For mode return the single most common datapoint from the data set. If
there are multiple modes with the same value, return the first encountered.
"""
import statistics
import sys
import random_numbers
import math

def main():
    amount_of_numbers_to_generate = sys.argv[1]
    try:
        amount_of_numbers_to_generate = int(amount_of_numbers_to_generate)
    except ValueError:
        amount_of_numbers_to_generate = 0
        while amount_of_numbers_to_generate <= 0:
            try:
                amount_of_numbers_to_generate = int(input("that was not a valid number greater than 0. Please try again with a new number: "))
            except ValueError:
                pass

    random_nums = random_numbers.generate(amount_of_numbers_to_generate, True)
    get_stats(random_nums)

def get_stats(numbers):
    mean = get_mean(numbers)
    median = get_median(numbers)
    mode = get_mode(numbers)
    variance = get_variance(numbers)
    stdev = get_stdev(numbers)
    print(f"mean: {mean}")
    print(f"median: {median}")
    print(f"mode: {mode}")
    print(f"variance: {variance}")
    print(f"standard deviation: {stdev}")

def get_mean(numbers):
    total_sum = sum(numbers)
    total_len = len(numbers)
    return total_sum / total_len

def get_median(numbers):
    total_len = len(numbers)
    if total_len == 1:
        return numbers[0]
    is_even = total_len % 2 == 0
    mid_index = total_len // 2
    if is_even:
        lower_mid_index = (total_len // 2) - 1
        return get_mean([numbers[mid_index], numbers[lower_mid_index]])
    return numbers[mid_index]

def get_mode(numbers):
    occurance_dict = {}
    for num in numbers:
        occurance_dict[num] = occurance_dict.get(num, 0) + 1
    return max(occurance_dict, key=occurance_dict.get)

def get_variance(numbers):
    mean = get_mean(numbers)
    return sum((x - mean) **2 for x in numbers) / (len(numbers) - 1)

def get_stdev(numbers):
    return math.sqrt(get_variance(numbers))


if __name__ == '__main__':
    main()
