import unittest
from qual_id.categories.music import Music
from test.unit.utils.category_helper import CategoryHelper


class TestMusic(unittest.TestCase):
    def setUp(self):
        self.music = Music()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.music)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
