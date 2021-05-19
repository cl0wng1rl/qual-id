import unittest
from qual_id.cli.info.app import App
from qual_id.cli.info.validator import Validator
from qual_id.cli.info.flag import Flag
from unittest.mock import Mock, patch


class TestApp(unittest.TestCase):
    COMMAND_NAME = "qid"
    INFO_FLAG = "--info"
    PARAMETER = "parameter"
    VALUE = "value"
    INFO_MESSAGE = "info"
    ERROR_MESSAGE = "error"

    @patch("qual_id.cli.info.app.Validator")
    @patch("qual_id.cli.info.app.Parser")
    def test__run__valid_arguments__info(
        self, mock_info_parser, mock_info_validator
    ):
        self.set_mock_info_parser(mock_info_parser.return_value)
        self.set_mock_info_validator(mock_info_validator.return_value, True)
        message = App.run(self.get_args())
        self.assertEqual(self.INFO_MESSAGE, message)

    @patch("qual_id.cli.info.app.Validator")
    @patch("qual_id.cli.info.app.Parser")
    def test__run__invalid_arguments__error(
        self, mock_info_parser, mock_info_validator
    ):
        self.set_mock_info_parser(mock_info_parser.return_value)
        self.set_mock_info_validator(mock_info_validator.return_value, False)
        message = App.run(self.get_args())
        self.assertEqual(self.ERROR_MESSAGE, message)

    def set_mock_info_parser(self, mock):
        mock.parse.return_value.message.return_value = self.INFO_MESSAGE

    def set_mock_info_validator(self, mock, is_valid):
        mock.is_valid.return_value = is_valid
        mock.error_message.return_value = self.ERROR_MESSAGE

    def get_args(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.PARAMETER, self.VALUE]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
