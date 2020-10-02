import unittest
from qual_id.categories.emotion import Emotion
from test.utils.category_helper import CategoryHelper


class TestEmotion(unittest.TestCase):
    def setUp(self):
        self.emotion = Emotion()

    def test__get_values__is_valid(self):
        self.assertTrue(CategoryHelper.get_values_is_valid(self.emotion))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
