import unittest
from qual_id.validator import Validator
from qual_id.validators import *

from unittest.mock import Mock, patch


class TestValidator(unittest.TestCase):
    @patch("qual_id.validator.PatternValidator")
    @patch("qual_id.validator.CollectionValidator")
    @patch("qual_id.validator.NumberValidator")
    @patch("qual_id.validator.FormatValidator")
    def test__is_valid__mock_validators_all_valid__true(
        self, mock_format_validator, mock_number_validator, mock_collection_validator, mock_pattern_validator
    ):  
        mock_format_validator.return_value.is_valid.return_value = True
        mock_number_validator.return_value.is_valid.return_value = True
        mock_collection_validator.return_value.is_valid.return_value = True
        mock_pattern_validator.return_value.is_valid.return_value = True

        validator = Validator(self.mock_config())
        validator.validate()
        self.assertTrue(validator.is_valid())

    @patch("qual_id.validator.PatternValidator")
    @patch("qual_id.validator.CollectionValidator")
    @patch("qual_id.validator.NumberValidator")
    @patch("qual_id.validator.FormatValidator")
    def test__error_message__pattern_validator_invalid__correct_error_message(
        self, mock_format_validator, mock_number_validator, mock_collection_validator, mock_pattern_validator
    ):
        mock_format_validator.return_value.is_valid.return_value = True
        mock_number_validator.return_value.is_valid.return_value = True
        mock_collection_validator.return_value.is_valid.return_value = True
        mock_pattern_validator.return_value.is_valid.return_value = False

        expected_error_message = "pattern error"
        mock_pattern_validator.return_value.error_message.return_value = expected_error_message

        validator = Validator(self.mock_config())
        validator.validate()
        self.assertFalse(validator.is_valid())
        self.assertEqual(expected_error_message, validator.error_message())

    @patch("qual_id.validator.PatternValidator")
    @patch("qual_id.validator.CollectionValidator")
    @patch("qual_id.validator.NumberValidator")
    @patch("qual_id.validator.FormatValidator")
    def test__error_message__collection_validator_invalid__correct_error_message(
        self, mock_format_validator, mock_number_validator, mock_collection_validator, mock_pattern_validator
    ):
        mock_format_validator.return_value.is_valid.return_value = True
        mock_number_validator.return_value.is_valid.return_value = True
        mock_collection_validator.return_value.is_valid.return_value = False
        mock_pattern_validator.return_value.is_valid.return_value = True

        expected_error_message = "collection error"
        mock_collection_validator.return_value.error_message.return_value = expected_error_message

        validator = Validator(self.mock_config())
        validator.validate()
        self.assertFalse(validator.is_valid())
        self.assertEqual(expected_error_message, validator.error_message())

    @patch("qual_id.validator.PatternValidator")
    @patch("qual_id.validator.CollectionValidator")
    @patch("qual_id.validator.NumberValidator")
    @patch("qual_id.validator.FormatValidator")
    def test__error_message__number_validator_invalid__correct_error_message(
        self, mock_format_validator, mock_number_validator, mock_collection_validator, mock_pattern_validator
    ):
        mock_format_validator.return_value.is_valid.return_value = True
        mock_number_validator.return_value.is_valid.return_value = False
        mock_collection_validator.return_value.is_valid.return_value = True
        mock_pattern_validator.return_value.is_valid.return_value = True

        expected_error_message = "number error"
        mock_number_validator.return_value.error_message.return_value = expected_error_message

        validator = Validator(self.mock_config())
        validator.validate()
        self.assertFalse(validator.is_valid())
        self.assertEqual(expected_error_message, validator.error_message())

    @patch("qual_id.validator.PatternValidator")
    @patch("qual_id.validator.CollectionValidator")
    @patch("qual_id.validator.NumberValidator")
    @patch("qual_id.validator.FormatValidator")
    def test__error_message__format_validator_invalid__correct_error_message(
        self, mock_format_validator, mock_number_validator, mock_collection_validator, mock_pattern_validator
    ):
        mock_format_validator.return_value.is_valid.return_value = False
        mock_number_validator.return_value.is_valid.return_value = True
        mock_collection_validator.return_value.is_valid.return_value = True
        mock_pattern_validator.return_value.is_valid.return_value = True

        expected_error_message = "format error"
        mock_format_validator.return_value.error_message.return_value = expected_error_message

        validator = Validator(self.mock_config())
        validator.validate()
        self.assertFalse(validator.is_valid())
        self.assertEqual(expected_error_message, validator.error_message())

    
    @patch("qual_id.validator.PatternValidator")
    @patch("qual_id.validator.CollectionValidator")
    @patch("qual_id.validator.NumberValidator")
    @patch("qual_id.validator.FormatValidator")
    def test__error_message__two_validators_invalid__second_validator_not_ran(
        self, mock_format_validator, mock_number_validator, mock_collection_validator, mock_pattern_validator
    ):
        mock_format_validator.return_value.is_valid.return_value = False
        mock_number_validator.return_value.is_valid.return_value = True
        mock_collection_validator.return_value.is_valid.return_value = False
        mock_pattern_validator.return_value.is_valid.return_value = True

        not_expected_error_message = "format error"
        mock_format_validator.return_value.error_message.return_value = not_expected_error_message
        expected_error_message = "collection error"
        mock_collection_validator.return_value.error_message.return_value = expected_error_message

        validator = Validator(self.mock_config())
        validator.validate()
        self.assertFalse(validator.is_valid())
        self.assertEqual(expected_error_message, validator.error_message())

    def mock_config(self):
        return Mock()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
