import unittest
from qual_id.categories.color import Color
import random


class TestColor(unittest.TestCase):
  def setUp(self):
    self.color = Color()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.color.get_values(), list)
    self.assertGreater(len(self.color.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.color.get_values():
      self.assertFalse(' ' in value)


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
