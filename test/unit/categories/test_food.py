import unittest
from qual_id.categories.food import Food
from test.unit.utils.category_helper import CategoryHelper


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.food)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
