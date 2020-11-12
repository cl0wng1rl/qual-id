import unittest
from qual_id.categories.flower import Flower
from test.unit.utils.category_helper import CategoryHelper


class TestFlower(unittest.TestCase):
    def setUp(self):
        self.flower = Flower()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.flower)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
