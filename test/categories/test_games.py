import unittest
from qual_id.categories.games import Games
import random


class TestAnimal(unittest.TestCase):
  def setUp(self):
    self.games = Games()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.games.get_values(), list)
    self.assertGreater(len(self.games.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.games.get_values():
      self.assertFalse(' ' in value)


if __name__ == '__main__':  # pragma: no cover
  unittest.main()