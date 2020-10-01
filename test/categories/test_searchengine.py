import unittest
from qual_id.categories.searchengine import SearchEngine
from test.utils.category_helper import CategoryHelper


class TestSeachEngine(unittest.TestCase):
  def setUp(self):
    self.searchengine = SearchEngine()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.searchengine))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()