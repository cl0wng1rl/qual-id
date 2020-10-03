import unittest
from qual_id.categories.color import Color
from test.utils.category_helper import CategoryHelper


class TestColor(unittest.TestCase):
    def setUp(self):
        self.color = Color()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.color)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
