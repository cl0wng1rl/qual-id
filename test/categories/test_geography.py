import unittest
from qual_id.categories.geography import Geography
from test.utils.category_helper import CategoryHelper


class TestGeography(unittest.TestCase):
    def setUp(self):
        self.geography = Geography()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.geography)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
