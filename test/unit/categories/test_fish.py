import unittest
from qual_id.categories.fish import Fish
from test.unit.utils.category_helper import CategoryHelper


class TestFish(unittest.TestCase):
    def setUp(self):
        self.fish = Fish()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.fish)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
