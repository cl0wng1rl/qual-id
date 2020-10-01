import unittest
from qual_id.categories.drink import Drink
from test.utils.category_helper import CategoryHelper


class TestDrink(unittest.TestCase):
  def setUp(self):
    self.drink = Drink()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.drink))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
