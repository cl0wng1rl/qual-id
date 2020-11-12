import unittest
from qual_id.categories.gem import Gem
from test.unit.utils.category_helper import CategoryHelper


class TestGem(unittest.TestCase):
    def setUp(self):
        self.gem = Gem()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.gem)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
