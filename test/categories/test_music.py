import unittest
from qual_id.categories.music import Music
from test.utils.category_helper import CategoryHelper


class TestMusic(unittest.TestCase):
    def setUp(self):
        self.music = Music()

    def test__get_values__is_valid(self):
        self.assertTrue(CategoryHelper.get_values_is_valid(self.music))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
