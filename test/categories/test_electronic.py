import unittest
from qual_id.categories.electronic import Electronic
import random


class TestElectronic(unittest.TestCase):
  def setUp(self):
    self.electronic = Electronic()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.electronic.get_values(), list)
    self.assertGreater(len(self.electronic.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.electronic.get_values():
      self.assertFalse(' ' in value)


if __name__ == '__main__':  # pragma: no cover
  unittest.main()