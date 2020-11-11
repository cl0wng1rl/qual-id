import unittest
from qual_id.categories.currency import Currency
from test.unit.utils.category_helper import CategoryHelper


class TestCurrency(unittest.TestCase):
    def setUp(self):
        self.currency = Currency()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.currency)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
