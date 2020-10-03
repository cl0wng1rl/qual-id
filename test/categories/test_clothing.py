import unittest
from qual_id.categories.clothing import Clothing
from test.utils.category_helper import CategoryHelper


class TestClothing(unittest.TestCase):
    def setUp(self):
        self.clothing = Clothing()

    def test__get_values__is_valid(self):
        self.assertTrue(CategoryHelper.get_values_is_valid(self.clothing))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
