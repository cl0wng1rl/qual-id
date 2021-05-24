import unittest
from qual_id.api import API
from unittest.mock import patch, Mock


class TestAPI(unittest.TestCase):
    """Unit Tests for Arguments"""

    QUAL_IDS = ["qual_id1", "qual_id2", "qual_id3"]
    FORMAT = "format_value"
    ERROR = "error message"
    CATEGORIES = ["category1", "category2"]
    ARGS = {
        "group": "group_value",
        "categories": "-".join(CATEGORIES),
        "number": "number_value",
        "format": FORMAT,
    }
    FORMATTED_ARGS = {
        "group": "group_value",
        "categories": CATEGORIES,
        "number": "number_value",
        "format": FORMAT,
    }

    @patch("qual_id.api.api.Formatter")
    @patch("qual_id.api.api.Validator")
    def test__run__invalid__correct_error_message(self, mock_validator, mock_formatter):
        """API -> run - invalid"""
        mock_validator.validate.return_value = self.ERROR
        mock_formatter.format_error.return_value = self.ERROR
        self.assertEqual(self.ERROR, API.run(self.ARGS))
        mock_validator.validate.assert_called_with(self.FORMATTED_ARGS)
        mock_formatter.format_error.assert_called_with(self.FORMAT, self.ERROR)

    @patch("qual_id.api.api.QualIDFactory")
    @patch("qual_id.api.api.Arguments")
    @patch("qual_id.api.api.Formatter")
    @patch("qual_id.api.api.Validator")
    def test__run__valid__correct_qual_ids(
        self, mock_validator, mock_formatter, mock_arguments, mock_factory
    ):
        """API -> run - valid"""
        mock_validator.validate.return_value = False
        mock_arguments.return_value = self.get_mock_arguments()
        mock_factory.get_qual_ids.return_value = self.QUAL_IDS
        mock_formatter.format_qual_ids.return_value = self.QUAL_IDS

        self.assertEqual(self.QUAL_IDS, API.run(self.ARGS))
        mock_validator.validate.assert_called_with(self.FORMATTED_ARGS)
        mock_arguments.assert_called_with(self.FORMATTED_ARGS)
        mock_factory.get_qual_ids.assert_called_with(mock_arguments.return_value)
        mock_formatter.format_qual_ids.assert_called_with(self.FORMAT, self.QUAL_IDS)

    def get_mock_arguments(self):
        mock = Mock()
        mock.get_format.return_value = self.FORMAT
        return mock
