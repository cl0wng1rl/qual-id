import unittest
from qual_id.cli.info.validator import Validator
from qual_id.cli.info.flag import Flag
from unittest.mock import patch


class TestValidator(unittest.TestCase):
    COMMAND_NAME = "qid"
    INFO_FLAG = "--info"
    CATEGORY = "category"
    CATEGORY_VALUE = "category-value"
    GROUP = "group"
    GROUP_VALUE = "group-value"
    FORMAT = "format"
    INVALID = "invalid"
    INVALID_VALUE = "invalid-value"

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__is_valid__category__true(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory)
        validator = Validator(self.get_valid_args__category())
        self.assertTrue(validator.is_valid())

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__is_valid__category_and_value__true(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory)
        validator = Validator(self.get_valid_args__category_and_value())
        self.assertTrue(validator.is_valid())

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__is_valid__group__true(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory)
        validator = Validator(self.get_valid_args__group())
        self.assertTrue(validator.is_valid())

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__is_valid__group_and_value__true(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory)
        validator = Validator(self.get_valid_args__group_and_value())
        self.assertTrue(validator.is_valid())

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__is_valid__format__true(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory)
        validator = Validator(self.get_valid_args__format())
        self.assertTrue(validator.is_valid())

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__is_valid__format_and_value__false(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory)
        validator = Validator(self.get_invalid_args__format_and_value())
        self.assertFalse(validator.is_valid())

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__is_valid__invalid_parameter__false(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory)
        validator = Validator(self.get_invalid_args__invalid_parameter())
        self.assertFalse(validator.is_valid())

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__is_valid__invalid_value__false(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory, False)
        validator = Validator(self.get_invalid_args__invalid_value())
        self.assertFalse(validator.is_valid())

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__error_message__format_and_value__false(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory)
        validator = Validator(self.get_invalid_args__format_and_value())
        expected_message = "invalid value: {0}".format(self.INVALID_VALUE)
        self.assertEqual(expected_message, validator.error_message())

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__error_message__invalid_parameter__false(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory)
        validator = Validator(self.get_invalid_args__invalid_parameter())
        expected_message = "invalid info value: {0}".format(self.INVALID)
        self.assertEqual(expected_message, validator.error_message())

    @patch("qual_id.cli.info.validator.InfoFactory")
    def test__error_message__invalid_value__false(self, mock_info_factory):
        self.set_mock_info_factory(mock_info_factory, False)
        validator = Validator(self.get_invalid_args__invalid_value())
        expected_message = "invalid {0} value: {1}".format(
            self.CATEGORY, self.INVALID_VALUE
        )
        self.assertEqual(expected_message, validator.error_message())

    def set_mock_info_factory(self, mock, has=True):
        mock.has.return_value = has

    def get_valid_args__category(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.CATEGORY]

    def get_valid_args__category_and_value(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.CATEGORY, self.CATEGORY_VALUE]

    def get_valid_args__group(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.GROUP]

    def get_valid_args__group_and_value(self):
        return [
            self.COMMAND_NAME,
            self.INFO_FLAG,
            self.GROUP,
            self.GROUP_VALUE,
        ]

    def get_valid_args__format(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.FORMAT]

    def get_invalid_args__format_and_value(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.FORMAT, self.INVALID_VALUE]

    def get_invalid_args__invalid_parameter(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.INVALID]

    def get_invalid_args__invalid_value(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.CATEGORY, self.INVALID_VALUE]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
