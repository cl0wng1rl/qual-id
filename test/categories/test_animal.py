import unittest
from qual_id.categories.animal import Animal
import random


class TestAnimal(unittest.TestCase):
  def setUp(self):
    self.animal = Animal()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.animal.get_values(), list)
    self.assertGreater(len(self.animal.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.animal.get_values():
      self.assertFalse(' ' in value)


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
