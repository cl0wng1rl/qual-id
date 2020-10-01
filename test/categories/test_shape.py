import unittest
from qual_id.categories.shape import Shape
import random


class TestShape(unittest.TestCase):
  def setUp(self):
    self.shape = Shape()

  def test__get_values__is_valid(self):
        self.assertTrue(CategoryHelper.get_values_is_valid(self.shape))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
