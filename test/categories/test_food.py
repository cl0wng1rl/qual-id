import unittest
from qual_id.categories.food import Food
import random


class TestFood(unittest.TestCase):
  def setUp(self):
    self.food = Food()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.food.get_values(), list)
    self.assertGreater(len(self.food.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.food.get_values():
      self.assertFalse(' ' in value)


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
