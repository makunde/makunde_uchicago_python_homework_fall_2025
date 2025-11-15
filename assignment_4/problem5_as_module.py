import stats
import random_numbers


def stats_on_100():
    random_nums = random_numbers.generate(100, False)
    stats.get_stats(random_nums)


stats_on_100()
