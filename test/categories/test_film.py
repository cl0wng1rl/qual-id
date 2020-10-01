import unittest
from qual_id.categories.film import Film
from test.utils.category_helper import CategoryHelper


class TestFilm(unittest.TestCase):
  def setUp(self):
    self.film = Film()

  def test__get_values__is_valid(self):
        self.assertTrue(CategoryHelper.get_values_is_valid(self.film))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
