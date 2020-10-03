import unittest
from qual_id.categories.brand import Brand
from test.utils.category_helper import CategoryHelper


class TestBrand(unittest.TestCase):
    def setUp(self):
        self.brand = Brand()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.brand)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
