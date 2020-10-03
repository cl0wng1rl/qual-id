import unittest
from qual_id.categories.sports import Sports
from test.utils.category_helper import CategoryHelper


class TestSports(unittest.TestCase):
    def setUp(self):
        self.sports = Sports()

    def test__get_values__is_valid(self):
        self.assertTrue(CategoryHelper.get_values_is_valid(self.sports))


if __name__ == '__main__': # pragma: no cover
    unittest.main()
