import unittest
from qual_id.categories.country import Country
from test.unit.utils.category_helper import CategoryHelper


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.country)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
