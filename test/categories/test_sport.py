import unittest
from qual_id.categories.sport import Sport
from test.utils.category_helper import CategoryHelper


class TestSport(unittest.TestCase):
    def setUp(self):
        self.sport = Sport()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.sport)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
