import unittest
from qual_id.categories.element import Element
from test.utils.category_helper import CategoryHelper


class TestElement(unittest.TestCase):
    def setUp(self):
        self.element = Element()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.element)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
