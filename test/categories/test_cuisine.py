import unittest
from qual_id.categories.cuisine import Cuisine
from test.utils.category_helper import CategoryHelper


class TestCuisine(unittest.TestCase):
    def setUp(self):
        self.cuisine = Cuisine()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.cuisine)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
