import unittest
from qual_id.categories.game import Game
import random


class TestGame(unittest.TestCase):
  def setUp(self):
    self.game = Game()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.game.get_values(), list)
    self.assertGreater(len(self.game.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.game.get_values():
      self.assertFalse(' ' in value)


if __name__ == '__main__':  # pragma: no cover
  unittest.main()