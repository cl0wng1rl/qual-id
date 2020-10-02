import unittest
from qual_id.categories.brand import Brand
from test.utils.category_helper import CategoryHelper


class TestBrand(unittest.TestCase):
  def setUp(self):
    self.brand = Brand()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.brand))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
