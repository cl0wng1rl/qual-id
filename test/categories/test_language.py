import unittest
from qual_id.categories.language import Language
from test.utils.category_helper import CategoryHelper


class TestLanguage(unittest.TestCase):
  def setUp(self):
    self.language = Language()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.language))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
