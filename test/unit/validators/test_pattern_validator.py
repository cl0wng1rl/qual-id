import unittest
from qual_id.validators.pattern_validator import PatternValidator
from qual_id.groups import GroupFactory
from unittest.mock import Mock, patch


class TestPatternValidator(unittest.TestCase):
    @patch.object(GroupFactory, "get")
    def test__validate__valid_pattern__is_valid_returns_true(
        self, mock_group_factory_get
    ):
        mock_group_factory_get.return_value = self.get_mock_group()
        categories = ["c1", "c2"]
        validator = PatternValidator("ValidGroupName", categories)
        validator.validate()
        self.assertTrue(validator.is_valid())

    @patch.object(GroupFactory, "get")
    def test__validate__pattern_with_too_many_categories__is_valid_returns_false(
        self, mock_group_factory_get
    ):
        mock_group_factory_get.return_value = self.get_mock_group()
        categories = ["c1", "c2", "c3", "c4", "c5", "c6"]
        validator = PatternValidator("ValidGroupName", categories)
        validator.validate()
        self.assertFalse(validator.is_valid())

    @patch.object(GroupFactory, "get")
    def test__validate__pattern_with_too_many_categories__error_message_returns_correct_message(
        self, mock_group_factory_get
    ):
        mock_group_factory_get.return_value = self.get_mock_group()
        categories = ["c1", "c2", "c3", "c4", "c5", "c6"]
        validator = PatternValidator("ValidGroupName", categories)
        validator.validate()
        expected_message = "number of categories should be between 1 and 5"
        self.assertEqual(expected_message, validator.error_message())

    @patch.object(GroupFactory, "get")
    def test__validate__pattern_with_invalid_categories__is_valid_returns_false(
        self, mock_group_factory_get
    ):
        mock_group_factory_get.return_value = (
            self.get_mock_group_with_invalid_category()
        )
        categories = ["c1", "c2"]
        validator = PatternValidator("ValidGroupName", categories)
        validator.validate()
        self.assertFalse(validator.is_valid())

    @patch.object(GroupFactory, "get")
    def test__validate__pattern_with_invalid_categories__error_message_returns_correct_message(
        self, mock_group_factory_get
    ):
        mock_group_factory_get.return_value = (
            self.get_mock_group_with_invalid_category()
        )
        categories = ["c1", "c2"]
        validator = PatternValidator("ValidGroupName", categories)
        validator.validate()
        expected_message = "invalid categories: ['c1']"
        self.assertEqual(expected_message, validator.error_message())

    def get_mock_group(self):
        mock = Mock()
        mock.invalid.return_value = []
        return mock

    def get_mock_group_with_invalid_category(self):
        mock = Mock()
        mock.invalid.return_value = ["c1"]
        return mock


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
