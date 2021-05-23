import unittest
from qual_id.cli.info.app import App
from qual_id.cli.info.flag import Flag
from unittest.mock import Mock, patch


class TestApp(unittest.TestCase):
    """Unit Tests for info.App"""

    FLAG = "flag"
    VALUE = "value"
    INFO = "info"
    INFO_MESSAGE = "info"

    def setUp(self):
        self.arguments = self.mock_arguments()

    @patch("qual_id.cli.info.app.InfoFactory")
    @patch("qual_id.cli.info.app.InfoMessage")
    def test__run__valid_arguments__info(
        self, mock_info_message, mock_info_factory
    ):
        """info.App -> run"""
        self.set_mock_info_factory(mock_info_factory)
        self.set_mock_info_message(mock_info_message)
        message = App.run(self.arguments)
        mock_info_factory.get.assert_called_with(self.FLAG, self.VALUE)
        mock_info_message.assert_called_with(self.FLAG, self.VALUE, self.INFO)
        self.assertEqual(self.INFO_MESSAGE, message)

    def mock_arguments(self):
        mock = Mock()
        mock.get_flag.return_value = self.FLAG
        mock.get_value.return_value = self.VALUE
        return mock

    def set_mock_info_message(self, mock):
        mock.return_value.message.return_value = self.INFO_MESSAGE

    def set_mock_info_factory(self, mock):
        mock.get = Mock()
        mock.get.return_value = self.INFO


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
