import unittest
from qual_id.categories.clothing import Clothing
from test.unit.utils.category_helper import CategoryHelper


class TestClothing(unittest.TestCase):
    def setUp(self):
        self.clothing = Clothing()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.clothing)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
