import unittest
from qual_id.categories.utensil import Utensil
from test.utils.category_helper import CategoryHelper


class TestUtensil(unittest.TestCase):
    def setUp(self):
        self.utensil = Utensil()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.utensil)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
