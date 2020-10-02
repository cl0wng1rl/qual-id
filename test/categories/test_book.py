import unittest
from qual_id.categories.book import Book
from test.utils.category_helper import CategoryHelper


class TestBook(unittest.TestCase):
  def setUp(self):
    self.book = Book()

  def test__get_values__is_valid(self):
        self.assertTrue(CategoryHelper.get_values_is_valid(self.book))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
