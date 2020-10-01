import unittest
from qual_id.categories.shape import Shape
import random


class TestShape(unittest.TestCase):
  def setUp(self):
    self.shape = Shape()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.shape.get_values(), list)
    self.assertGreater(len(self.shape.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.shape.get_values():
      self.assertFalse(' ' in value)


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
