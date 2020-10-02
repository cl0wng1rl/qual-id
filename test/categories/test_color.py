import unittest
from qual_id.categories.color import Color
from test.utils.category_helper import CategoryHelper


class TestColor(unittest.TestCase):
  def setUp(self):
    self.color = Color()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.color))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
