import unittest
from qual_id.cli import CLI
from unittest.mock import Mock, patch


class TestCLI(unittest.TestCase):
    COMMAND_NAME = "qid"
    PARAMETER = "parameter"
    INFO_FLAG = "--info"
    INFO_FLAG_SHORT = "--info"
    VALUE = "value"
    INFO_RESPONSE = "info response"
    MAIN_RESPONSE = "main response"

    @patch("qual_id.cli.cli.InfoApp")
    @patch("qual_id.cli.cli.App")
    def test__run__main_arguments__main_message(self, mock_main_app, mock_info_app):
        mock_main_app.run.return_value = self.MAIN_RESPONSE
        mock_info_app.run.return_value = self.INFO_RESPONSE
        self.assertEqual(self.MAIN_RESPONSE, CLI.run(self.get_args__main()))

    @patch("qual_id.cli.cli.InfoApp")
    @patch("qual_id.cli.cli.App")
    def test__run__info_arguments__info_message(self, mock_main_app, mock_info_app):
        mock_main_app.run.return_value = self.MAIN_RESPONSE
        mock_info_app.run.return_value = self.INFO_RESPONSE
        self.assertEqual(self.INFO_RESPONSE, CLI.run(self.get_args__info()))

    @patch("qual_id.cli.cli.InfoApp")
    @patch("qual_id.cli.cli.App")
    def test__run__info_short_args__info_message(self, mock_main_app, mock_info_app):
        mock_main_app.run.return_value = self.MAIN_RESPONSE
        mock_info_app.run.return_value = self.INFO_RESPONSE
        self.assertEqual(self.INFO_RESPONSE, CLI.run(self.get_args__info_short()))

    def get_args__main(self):
        return [self.COMMAND_NAME, self.PARAMETER, self.VALUE]

    def get_args__info(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.VALUE]

    def get_args__info_short(self):
        return [self.COMMAND_NAME, self.INFO_FLAG_SHORT, self.VALUE]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
