import unittest
from qual_id.cli.main.app import App
from unittest.mock import Mock, patch


class TestApp(unittest.TestCase):
    """Unit Tests for main.App"""

    RESPONSE = "qual id"

    @patch("qual_id.cli.main.app.Response")
    def test__run__valid_arguments__info(self, mock_response):
        """main.App -> run"""
        self.set_mock_response(mock_response.return_value)
        mock_arguments = Mock()
        response = App.run(mock_arguments)
        self.assertEqual(self.RESPONSE, response)

    def set_mock_response(self, mock):
        mock.get_response_obj.return_value = self.RESPONSE


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
