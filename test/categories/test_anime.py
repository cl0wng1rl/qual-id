import unittest
from qual_id.categories.anime import Anime
from test.utils.category_helper import CategoryHelper


class TestAnime(unittest.TestCase):
    def setUp(self):
        self.anime = Anime()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.anime)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
