import unittest
from qual_id.categories.food import Food
from test.utils.category_helper import CategoryHelper


class TestFood(unittest.TestCase):
  def setUp(self):
    self.food = Food()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.food))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
