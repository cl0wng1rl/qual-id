import unittest
from qual_id.category_map import CategoryMap
from qual_id.pattern import Pattern
from unittest.mock import Mock, call, patch


class TestPattern(unittest.TestCase):
    CATEGORY_KEYS = ["first_category", "second_category"]
    RANDOM_KEY = "random"

    def test__get_categories__pattern__returns_array_of_correct_length(self):
        pattern_string = "-".join(self.CATEGORY_KEYS[:2])
        mock_category_map = self.get_mock_category_map()
        pattern = Pattern(pattern_string, mock_category_map)

        categories = pattern.get_categories()

        self.assertEqual(len(categories), 2)

    def test__get_categories__pattern__correctly_calls_get_on_category_map(self):
        pattern_string = "-".join(self.CATEGORY_KEYS[:2])
        mock_category_map = self.get_mock_category_map()
        pattern = Pattern(pattern_string, mock_category_map)

        pattern.get_categories()

        expected_calls = [call(self.CATEGORY_KEYS[0]), call(self.CATEGORY_KEYS[1])]
        self.assertEqual(expected_calls, mock_category_map.get.call_args_list)

    def test__get_categories__pattern_with_randoms__correctly_calls_get_on_category_map(
        self,
    ):
        pattern_string = "-".join([self.RANDOM_KEY] * 2)
        mock_category_map = self.get_mock_category_map()
        mock_category_map.categories.return_value = [self.CATEGORY_KEYS[0]]
        pattern = Pattern(pattern_string, mock_category_map)

        categories = pattern.get_categories()

        self.assertEqual(len(categories), 2)
        expected_calls = [call(self.CATEGORY_KEYS[0]), call(self.CATEGORY_KEYS[0])]
        self.assertEqual(expected_calls, mock_category_map.get.call_args_list)

    def test__error__valid_pattern__returns_false(self):
        pattern_string = "-".join(self.CATEGORY_KEYS[:2])
        mock_category_map = self.get_mock_category_map()
        pattern = Pattern(pattern_string, mock_category_map)

        result = pattern.error()

        self.assertFalse(result)

    def test__error__pattern_with_invalid_category__returns_error_message(self):
        pattern_string = "-".join(self.CATEGORY_KEYS[:2])
        mock_category_map = self.get_mock_category_map()
        invalid = [self.CATEGORY_KEYS[0]]
        mock_category_map.invalid.return_value = invalid
        pattern = Pattern(pattern_string, mock_category_map)

        result = pattern.error()

        self.assertEqual("invalid categories: %s" % (invalid), result)

    def test__error__empty_pattern__returns_error_message(self):
        mock_category_map = self.get_mock_category_map()
        pattern = Pattern("", mock_category_map)

        result = pattern.error()

        self.assertEqual("number of categories should be between 1 and 5", result)

    def test__error__pattern_with_too_many_categories__returns_error_message(self):
        pattern_string = "-".join([self.CATEGORY_KEYS[0]] * 6)
        mock_category_map = self.get_mock_category_map()
        pattern = Pattern(pattern_string, mock_category_map)

        result = pattern.error()

        self.assertEqual("number of categories should be between 1 and 5", result)

    def get_mock_category_map(self):
        mock = Mock()
        mock.get.return_value = self.mock_category()
        mock.invalid.return_value = []
        return mock

    def mock_category(self):
        return Mock()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
