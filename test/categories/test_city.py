import unittest
from qual_id.categories.city import City
from test.utils.category_helper import CategoryHelper


class TestCity(unittest.TestCase):
  def setUp(self):
    self.city = City()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.city))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
