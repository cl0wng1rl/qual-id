import unittest
from qual_id.categories.book import Book
from test.utils.category_helper import CategoryHelper


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.book)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
