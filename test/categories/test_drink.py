import unittest
from qual_id.categories.drink import Instrument
import random


class TestDrink(unittest.TestCase):
  def setUp(self):
    self.drink = Drink()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.drink.get_values(), list)
    self.assertGreater(len(self.drink.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.drink.get_values():
      self.assertFalse(' ' in value)


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
