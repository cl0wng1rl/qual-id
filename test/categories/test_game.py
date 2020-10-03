import unittest
from qual_id.categories.game import Game
from test.utils.category_helper import CategoryHelper


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.game)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
