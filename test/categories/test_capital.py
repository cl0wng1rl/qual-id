import unittest
from qual_id.categories.capital import Capital
from test.utils.category_helper import CategoryHelper


class TestCapital(unittest.TestCase):
    def setUp(self):
        self.capital = Capital()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.capital)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
