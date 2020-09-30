import unittest
from qual_id.categories.adjective import Adjective
import random


class TestAdjectives(unittest.TestCase):
  def setUp(self):
    self.adjective = Adjective()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.adjective.get_values(), list)
    self.assertGreater(len(self.adjective.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.adjective.get_values():
      self.assertFalse(' ' in value)


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
