import unittest
from qual_id.categories.wine import Wine
from test.unit.utils.category_helper import CategoryHelper


class TestWine(unittest.TestCase):
    def setUp(self):
        self.wine = Wine()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.wine)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
