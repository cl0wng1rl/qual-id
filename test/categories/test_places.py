import unittest
from qual_id.categories.country import Country
from test.utils.category_helper import CategoryHelper


class TestCountryl(unittest.TestCase):
  def setUp(self):
    self.country = Country()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.country))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
