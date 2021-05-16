import unittest
from qual_id.collection import Collection
from qual_id.pattern import Pattern
from unittest.mock import Mock, call, patch


class TestPattern(unittest.TestCase):
    CATEGORY_KEYS = ["first_category", "second_category"]
    PATTERN = "-".join(CATEGORY_KEYS[:2])
    RANDOM_KEY = "random"

    def test__get_categories__pattern__returns_array_of_correct_length(self):
        pattern_string = TestPattern.PATTERN
        mock_collection = self.get_mock_collection()
        pattern = Pattern(pattern_string, mock_collection)

        categories = pattern.get_categories()

        self.assertEqual(len(categories), 2)

    def test__get_categories__pattern__correctly_calls_get_on_collection(self):
        pattern_string = TestPattern.PATTERN
        mock_collection = self.get_mock_collection()
        pattern = Pattern(pattern_string, mock_collection)

        pattern.get_categories()

        expected_calls = [call(self.CATEGORY_KEYS[0]), call(self.CATEGORY_KEYS[1])]
        self.assertEqual(expected_calls, mock_collection.get.call_args_list)

    def test__get_categories__pattern_with_randoms__correctly_calls_get_on_collection(
        self,
    ):
        pattern_string = "-".join([self.RANDOM_KEY] * 2)
        mock_collection = self.get_mock_collection()
        mock_collection.random.return_value = self.CATEGORY_KEYS[0]
        pattern = Pattern(pattern_string, mock_collection)

        categories = pattern.get_categories()

        self.assertEqual(len(categories), 2)
        expected_calls = [call(self.CATEGORY_KEYS[0]), call(self.CATEGORY_KEYS[0])]
        self.assertEqual(expected_calls, mock_collection.get.call_args_list)

    def get_mock_collection(self):
        mock = Mock()
        mock.get.return_value = self.mock_category()
        mock.invalid.return_value = []
        return mock

    def mock_category(self):
        return Mock()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
