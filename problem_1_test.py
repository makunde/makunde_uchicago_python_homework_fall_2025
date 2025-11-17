import unittest
from unittest.mock import patch
import problem_1_temperature_converter


class TestTemperatureConverter(unittest.TestCase):
    def test_freezing_point(self):
        result = problem_1_temperature_converter.temp_converter(32)
        self.assertEqual(result, 0.0)

    def test_boiling_point(self):
        result = problem_1_temperature_converter.temp_converter(212)
        self.assertEqual(result, 100.0)

    def test_negative_temperature(self):
        result = problem_1_temperature_converter.temp_converter(-40)
        self.assertEqual(result, -40.0)

    def test_typical_temperature(self):
        result = problem_1_temperature_converter.temp_converter(98)
        self.assertEqual(result, 36.67)

    def test_zero_fahrenheit(self):
        result = problem_1_temperature_converter.temp_converter(0)
        self.assertEqual(result, -17.78)

    # Test validate_user_input function
    def test_validate_valid_number_string(self):
        result = problem_1_temperature_converter.validate_user_input("98")
        self.assertEqual(result, 98)

    def test_validate_negative_string(self):
        result = problem_1_temperature_converter.validate_user_input("-40")
        self.assertEqual(result, -40)

    @patch("builtins.input", return_value="98")
    def test_validate_invalid_then_valid(self, mock_input):
        result = problem_1_temperature_converter.validate_user_input("invalid")
        self.assertEqual(result, 98)
        mock_input.assert_called_once()

    @patch("builtins.input", side_effect=["still invalid", "75"])
    def test_validate_multiple_invalid_inputs(self, mock_input):
        result = problem_1_temperature_converter.validate_user_input("first invalid")
        self.assertEqual(result, 75)
        self.assertEqual(mock_input.call_count, 2)


if __name__ == "__main__":
    unittest.main()
