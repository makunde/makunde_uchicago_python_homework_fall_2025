import unittest
import statistics
import stats


class TestGetMean(unittest.TestCase):
    def test_mean_simple_list(self):
        numbers = [1, 2, 3, 4, 5]
        result = round(stats.get_mean(numbers), 2)
        expected = round(statistics.mean(numbers), 2)
        self.assertEqual(result, expected)

    def test_mean_single_element(self):
        numbers = [10]
        result = round(stats.get_mean(numbers), 2)
        expected = round(statistics.mean(numbers), 2)
        self.assertEqual(result, expected)

    def test_mean_negative_numbers(self):
        numbers = [-20, -15, -10, -5]
        result = round(stats.get_mean(numbers), 2)
        expected = round(statistics.mean(numbers), 2)
        self.assertEqual(result, expected)

    def test_mean_mixed_numbers(self):
        numbers = [-20, -10, 0, 10, 20]
        result = round(stats.get_mean(numbers), 2)
        expected = round(statistics.mean(numbers), 2)
        self.assertEqual(result, expected)

    def test_mean_decimals(self):
        numbers = [1.5, 2.7, 3.3, 4.8]
        result = round(stats.get_mean(numbers), 2)
        expected = round(statistics.mean(numbers), 2)
        self.assertEqual(result, expected)


class TestGetMedian(unittest.TestCase):
    def test_median_odd_length(self):
        numbers = [1, 2, 3, 4, 5]
        result = round(stats.get_median(numbers), 2)
        expected = round(statistics.median(numbers), 2)
        self.assertEqual(result, expected)

    def test_median_even_length(self):
        numbers = [1, 2, 3, 4]
        result = round(stats.get_median(numbers), 2)
        expected = round(statistics.median(numbers), 2)
        self.assertEqual(result, expected)

    def test_median_single_element(self):
        numbers = [7]
        result = round(stats.get_median(numbers), 2)
        expected = round(statistics.median(numbers), 2)
        self.assertEqual(result, expected)

    def test_median_two_elements(self):
        numbers = [5, 15]
        result = round(stats.get_median(numbers), 2)
        expected = round(statistics.median(numbers), 2)
        self.assertEqual(result, expected)

    def test_median_large_list(self):
        numbers = list(range(1, 100))
        result = round(stats.get_median(numbers), 2)
        expected = round(statistics.median(numbers), 2)
        self.assertEqual(result, expected)


class TestGetMode(unittest.TestCase):
    def test_mode_clear_winner(self):
        numbers = [1, 2, 2, 2, 3, 4]
        result = stats.get_mode(numbers)
        expected = statistics.mode(numbers)
        self.assertEqual(result, expected)

    def test_mode_all_same(self):
        numbers = [5, 5, 5, 5]
        result = stats.get_mode(numbers)
        expected = statistics.mode(numbers)
        self.assertEqual(result, expected)

    def test_mode_single_element(self):
        numbers = [42]
        result = stats.get_mode(numbers)
        expected = statistics.mode(numbers)
        self.assertEqual(result, expected)

    def test_mode_at_end(self):
        numbers = [1, 2, 3, 4, 4, 4]
        result = stats.get_mode(numbers)
        expected = statistics.mode(numbers)
        self.assertEqual(result, expected)


class TestGetVariance(unittest.TestCase):
    def test_variance_simple_list(self):
        numbers = [2, 4, 6, 8]
        result = round(stats.get_variance(numbers), 2)
        expected = round(statistics.variance(numbers), 2)
        self.assertEqual(result, expected)

    def test_variance_all_same(self):
        numbers = [5, 5, 5, 5]
        result = round(stats.get_variance(numbers), 2)
        expected = round(statistics.variance(numbers), 2)
        self.assertEqual(result, expected)

    def test_variance_two_elements(self):
        numbers = [1, 3]
        result = round(stats.get_variance(numbers), 2)
        expected = round(statistics.variance(numbers), 2)
        self.assertEqual(result, expected)

    def test_variance_negative_numbers(self):
        numbers = [-5, -3, -1, 1, 3, 5]
        result = round(stats.get_variance(numbers), 2)
        expected = round(statistics.variance(numbers), 2)
        self.assertEqual(result, expected)

    def test_variance_large_list(self):
        numbers = list(range(1, 50))
        result = round(stats.get_variance(numbers), 2)
        expected = round(statistics.variance(numbers), 2)
        self.assertEqual(result, expected)


class TestGetStdev(unittest.TestCase):
    def test_stdev_simple_list(self):
        numbers = [2, 4, 6, 8]
        result = round(stats.get_stdev(numbers), 2)
        expected = round(statistics.stdev(numbers), 2)
        self.assertEqual(result, expected)

    def test_stdev_all_same(self):
        numbers = [10, 10, 10]
        result = round(stats.get_stdev(numbers), 2)
        expected = round(statistics.stdev(numbers), 2)
        self.assertEqual(result, expected)

    def test_stdev_two_elements(self):
        numbers = [5, 15]
        result = round(stats.get_stdev(numbers), 2)
        expected = round(statistics.stdev(numbers), 2)
        self.assertEqual(result, expected)

    def test_stdev_negative_numbers(self):
        numbers = [-10, -5, 0, 5, 10]
        result = round(stats.get_stdev(numbers), 2)
        expected = round(statistics.stdev(numbers), 2)
        self.assertEqual(result, expected)

    def test_stdev_large_list(self):
        numbers = list(range(1, 100))
        result = round(stats.get_stdev(numbers), 2)
        expected = round(statistics.stdev(numbers), 2)
        self.assertEqual(result, expected)


class TestGetStats(unittest.TestCase):
    def test_get_stats_returns_dict(self):
        numbers = [1, 2, 3, 4, 5]
        result = stats.get_stats(numbers)
        self.assertIsInstance(result, dict)

    def test_get_stats_has_all_keys(self):
        numbers = [1, 2, 3, 4, 5]
        result = stats.get_stats(numbers)
        expected_keys = ["mean", "median", "mode", "variance", "standard_deviation"]
        for key in expected_keys:
            self.assertIn(key, result)

    def test_get_stats_values_match_statistics_module(self):
        numbers = [2, 4, 6, 8, 10, 12]
        result = stats.get_stats(numbers)

        self.assertEqual(round(result["mean"], 2), round(statistics.mean(numbers), 2))
        self.assertEqual(
            round(result["median"], 2), round(statistics.median(numbers), 2)
        )
        self.assertEqual(result["mode"], statistics.mode(numbers))
        self.assertEqual(
            round(result["variance"], 2), round(statistics.variance(numbers), 2)
        )
        self.assertEqual(
            round(result["standard_deviation"], 2), round(statistics.stdev(numbers), 2)
        )

    def test_get_stats_with_random_data(self):
        numbers = [7, 9, 12, 15, 18, 23, 27, 31, 35, 42]
        result = stats.get_stats(numbers)

        self.assertEqual(round(result["mean"], 2), round(statistics.mean(numbers), 2))
        self.assertEqual(
            round(result["median"], 2), round(statistics.median(numbers), 2)
        )
        self.assertEqual(result["mode"], statistics.mode(numbers))
        self.assertEqual(
            round(result["variance"], 2), round(statistics.variance(numbers), 2)
        )
        self.assertEqual(
            round(result["standard_deviation"], 2), round(statistics.stdev(numbers), 2)
        )


if __name__ == "__main__":
    unittest.main()
