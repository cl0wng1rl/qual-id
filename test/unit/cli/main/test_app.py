import unittest
from qual_id.cli.main.app import App
from qual_id.cli.main.validator import Validator
from qual_id.cli.main.flag import Flag
from unittest.mock import Mock, patch


class TestApp(unittest.TestCase):
    COMMAND_NAME = "qid"
    PARAMETER = "parameter"
    VALUE = "value"
    RESPONSE = "qual id"
    ERROR_MESSAGE = "error"

    @patch("qual_id.cli.main.app.Validator")
    @patch("qual_id.cli.main.app.Parser")
    @patch("qual_id.cli.main.app.Response")
    def test__run__valid_arguments__info(
        self, mock_response, mock_parser, mock_validator
    ):
        self.set_mock_response(mock_response.return_value)
        self.set_mock_parser(mock_parser.return_value)
        self.set_mock_validator(mock_validator.return_value, True)
        response = App.run(self.get_args())
        self.assertEqual(self.RESPONSE, response)

    @patch("qual_id.cli.main.app.Validator")
    @patch("qual_id.cli.main.app.Parser")
    @patch("qual_id.cli.main.app.Response")
    def test__run__invalid_arguments__error(
        self, mock_response, mock_parser, mock_validator
    ):
        self.set_mock_response(mock_response.return_value)
        self.set_mock_parser(mock_parser.return_value)
        self.set_mock_validator(mock_validator.return_value, False)
        message = App.run(self.get_args())
        self.assertEqual(self.ERROR_MESSAGE, message)

    def set_mock_response(self, mock):
        mock.get_response_obj.return_value = self.RESPONSE

    def set_mock_parser(self, mock):
        mock.parse.return_value.message.return_value = self.RESPONSE

    def set_mock_validator(self, mock, is_valid):
        mock.is_valid.return_value = is_valid
        mock.error_message.return_value = self.ERROR_MESSAGE

    def get_args(self):
        return [self.COMMAND_NAME, self.PARAMETER, self.VALUE]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
