import statistics


def main():
    file = open(
        "/Users/georg/Documents/uchicago_concepts_of_programming/assignment_4/numbers.txt"
    )
    numbers = [int(line) for line in file.read().splitlines()]
    get_stats(numbers)


def get_stats(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    mode = statistics.mode(numbers)
    variance = statistics.variance(numbers)
    stdev = statistics.stdev(numbers)
    print(f"mean: {mean}")
    print(f"median: {median}")
    print(f"mode: {mode}")
    print(f"variance: {variance}")
    print(f"standard deviation: {stdev}")


if __name__ == "__main__":
    main()
