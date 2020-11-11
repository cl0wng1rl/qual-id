import unittest
from qual_id.pattern import Pattern
from qual_id.category_map import CategoryMap
from qual_id.category_map_factory import CategoryMapFactory
from qual_id.validator import Validator
from unittest.mock import Mock, call, patch


class TestValidator(unittest.TestCase):
    @patch.object(CategoryMapFactory, "has")
    @patch.object(CategoryMapFactory, "get")
    @patch.object(Pattern, "error")
    def test__error__valid_pattern_and_collection__false(
        self, mock_error, mock_get, mock_has
    ):
        mock_has.return_value = True
        mock_get.return_value = self.get_mock_category_map()
        mock_error.return_value = False

        pattern_string = "pattern"
        collection_string = "collection"

        validator = Validator(pattern_string, collection_string)
        self.assertFalse(validator.error())

    @patch.object(CategoryMapFactory, "has")
    @patch.object(CategoryMapFactory, "get")
    @patch("qual_id.pattern.Pattern")
    def test__error__invalid_collection__error_message(
        self, mock_error, mock_get, mock_has
    ):
        mock_has.return_value = False

        pattern_string = "pattern"
        collection_string = "invalid_collection"

        validator = Validator(pattern_string, collection_string)

        expected_error_message = "invalid collection: " + collection_string
        self.assertEqual(expected_error_message, validator.error())

    @patch.object(CategoryMapFactory, "has")
    @patch.object(CategoryMapFactory, "get")
    @patch.object(Pattern, "error")
    def test__error__invalid_pattern__error_message(
        self, mock_error, mock_get, mock_has
    ):
        mock_has.return_value = True
        mock_get.return_value = self.get_mock_category_map()

        mock_error_message = "error message"
        mock_error.return_value = mock_error_message

        pattern_string = "pattern"
        collection_string = "collection"

        validator = Validator(pattern_string, collection_string)
        self.assertEqual(mock_error_message, validator.error())

    @patch.object(CategoryMapFactory, "has")
    @patch.object(CategoryMapFactory, "get")
    @patch("qual_id.pattern.Pattern")
    def test__valid_pattern__valid_pattern_and_collection__returns_pattern(
        self, mock_error, mock_get, mock_has
    ):
        mock_has.return_value = True
        mock_get.return_value = self.get_mock_category_map()
        mock_error.return_value = False

        pattern_string = "pattern"
        collection_string = "collection"

        validator = Validator(pattern_string, collection_string)
        validator.error()
        self.assertIsInstance(validator.valid_pattern(), Pattern)

    def get_mock_category_map(self):
        mock = Mock()
        mock.get.return_value = self.mock_category()
        mock.invalid.return_value = []
        return mock

    def mock_category(self):
        return Mock()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
