import unittest
from qual_id.categories.game import Game
from test.utils.category_helper import CategoryHelper


class TestGame(unittest.TestCase):
  def setUp(self):
    self.game = Game()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.game))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
