import unittest
from qual_id.categories.spice import Spice
from test.unit.utils.category_helper import CategoryHelper


class TestSpice(unittest.TestCase):
    def setUp(self):
        self.spice = Spice()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.spice)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
