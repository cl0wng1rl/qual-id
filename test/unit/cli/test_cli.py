import unittest
from qual_id.cli import CLI
from qual_id.parser.command import Command
from unittest.mock import Mock, patch


class TestCLI(unittest.TestCase):
    """Unit Tests for CLI"""

    COMMAND_NAME = "qid"
    PARAMETER = "parameter"
    VALUE = "value"
    INFO_RESPONSE = "info response"
    MAIN_RESPONSE = "main response"

    @patch("qual_id.cli.cli.Parser")
    @patch("qual_id.cli.cli.InfoApp")
    @patch("qual_id.cli.cli.Response")
    def test__run__main_arguments__main_message(
        self, mock_response, mock_info_app, mock_parser
    ):
        """CLI -> run - main arguments"""
        mock_parser.parse.return_value = self.get_mock_arguments(Command.MAIN)
        mock_response.return_value.get_response_obj.return_value = self.MAIN_RESPONSE
        mock_info_app.run.return_value = self.INFO_RESPONSE
        self.assertEqual(self.MAIN_RESPONSE, CLI.run(self.get_args()))

    @patch("qual_id.cli.cli.Parser")
    @patch("qual_id.cli.cli.InfoApp")
    @patch("qual_id.cli.cli.Response")
    def test__run__info_arguments__info_message(
        self, mock_response, mock_info_app, mock_parser
    ):
        """CLI -> run - info arguments"""
        mock_parser.parse.return_value = self.get_mock_arguments(Command.INFO)
        mock_response.return_value.get_response_obj.return_value = self.MAIN_RESPONSE
        mock_info_app.run.return_value = self.INFO_RESPONSE
        self.assertEqual(self.INFO_RESPONSE, CLI.run(self.get_args()))

    def get_mock_arguments(self, command):
        mock = Mock()
        mock.get_command.return_value = command
        return mock

    def get_args(self):
        return [self.COMMAND_NAME, self.PARAMETER, self.VALUE]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
