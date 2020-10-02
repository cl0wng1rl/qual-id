import unittest
from qual_id.categories.geography import Geography
from test.utils.category_helper import CategoryHelper


class TestGeography(unittest.TestCase):
    def setUp(self):
        self.geography = Geography()

    def test__get_values__is_valid(self):
        self.assertTrue(CategoryHelper.get_values_is_valid(self.geography))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
