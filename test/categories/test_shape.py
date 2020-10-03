import unittest
from qual_id.categories.shape import Shape
from test.utils.category_helper import CategoryHelper


class TestShape(unittest.TestCase):
    def setUp(self):
        self.shape = Shape()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.shape)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
