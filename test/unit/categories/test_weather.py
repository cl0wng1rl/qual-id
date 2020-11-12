import unittest
from qual_id.categories.weather import Weather
from test.unit.utils.category_helper import CategoryHelper


class TestWeather(unittest.TestCase):
    def setUp(self):
        self.weather = Weather()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.weather)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
