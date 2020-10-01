import unittest
from qual_id.categories.country import Country
from test.utils.category_helper import CategoryHelper


class TestCountry(unittest.TestCase):
  def setUp(self):
    self.country = Country()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.country.get_values(), list)
    self.assertGreater(len(self.country.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.country.get_values():
      self.assertFalse(' ' in value)

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.country))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
