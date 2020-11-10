import unittest
from qual_id.pattern import Pattern
from unittest.mock import Mock, call


class TestPattern(unittest.TestCase):
    def test__get_category_options__returns_non_empty_list(self):
        self.pattern = Pattern("", self.mock_category_map())
        self.assertGreater(len(self.pattern.get_category_options()), 0)

    def test__get_category_options__returns_alphabetically_ordered_list(self):
        self.pattern = Pattern("", self.mock_category_map())
        categories = self.pattern.get_category_options()
        error_message = "categories should be listed in alphabetical order"
        self.assertEqual(categories, sorted(categories), error_message)

    def test__has_acceptable_categories_length__valid_number_of_categories_returns_true(
        self,
    ):
        self.pattern = Pattern("test_pattern", self.mock_category_map())
        categories = self.pattern.get_category_options()

        self.pattern = Pattern("-".join([categories[0], categories[1]]))
        self.assertTrue(self.pattern.has_acceptable_categories_length())

    def test__get_nonexistent_categories__nonempty_invalid_category_list__returns_false(
        self,
    ):
        self.pattern = Pattern("invalid_pattern", self.mock_category_map())
        self.assertTrue(len(self.pattern.get_nonexistent_categories()) > 0)

    def test__has_acceptable_categories_length__pattern_with_more_than_5_categories__returns_false(
        self,
    ):
        self.pattern = Pattern("test_pattern", self.mock_category_map())
        categories = self.pattern.get_category_options()

        self.pattern = Pattern("-".join([categories[0]] * 6))
        self.assertFalse(self.pattern.has_acceptable_categories_length())

    def test__has_acceptable_categories_length__empty_pattern__returns_false(self):
        self.pattern = Pattern("", self.mock_category_map())
        self.assertFalse(self.pattern.has_acceptable_categories_length())

    def test__get_categories__pattern__returns_array_of_correct_length(self):
        first_category_name, second_category_name = "first_category", "second_category"
        pattern_string = "-".join([first_category_name, second_category_name])

        mock_category_map = self.mock_category_map()
        self.pattern = Pattern(pattern_string, mock_category_map)

        categories = self.pattern.get_categories()

        self.assertEqual(len(categories), 2)

    def test__get_categories__pattern__correctly_calls_get_on_category_map(self):
        first_category_name, second_category_name = "first_category", "second_category"
        pattern_string = "-".join([first_category_name, second_category_name])

        mock_category_map = self.mock_category_map()

        self.pattern = Pattern(pattern_string, mock_category_map)
        self.pattern.get_categories()

        expected_calls = [call(first_category_name), call(second_category_name)]
        self.assertEqual(expected_calls, mock_category_map.get.call_args_list)

    def test__get_categories__pattern_with_randoms__returns_array_of_correct_length(
        self,
    ):
        self.pattern = Pattern("-".join(["random"] * 2))
        categories = self.pattern.get_categories()
        self.assertEqual(len(categories), 2)
        [self.assertNotEqual(category, None) for category in categories]

    def mock_category_map(self):
        mock = Mock()
        mock.get.return_value = self.mock_category()
        return mock

    def mock_category(self):
        return Mock()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
