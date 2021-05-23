import unittest
from qual_id.pattern import Pattern
from qual_id.parser.command import Command
from qual_id.response import Response
from unittest.mock import Mock, call, patch


class TestResponse(unittest.TestCase):
    """Unit Tests for Response"""

    CSV = "csv"
    JSON = "json"
    QUAL_IDS = ["qual_id1", "qual_id2", "qual_id3"]
    CATEGORIES = ["category1", "category2"]
    GROUP = "all"
    NUMBER = 3

    @patch("qual_id.response.Pattern")
    def test__get_response_obj__json_format__correct_object(self, mock_pattern):
        """Response -> get_response_obj - JSON format"""
        arguments = self.mock_arguments(self.JSON)
        mock_pattern.return_value = self.get_mock_pattern()

        response = Response(arguments)
        expected = {"data": self.QUAL_IDS}
        self.assertEqual(expected, response.get_response_obj())

    @patch("qual_id.response.Pattern")
    def test__get_response_obj__csv_format__correct_object(self, mock_pattern):
        """Response -> get_response_obj - CSV format"""
        arguments = self.mock_arguments(self.CSV)
        mock_pattern.return_value = self.get_mock_pattern()

        response = Response(arguments)

        expected = ",".join(self.QUAL_IDS)
        self.assertEqual(expected, response.get_response_obj())

    @patch("qual_id.response.Pattern")
    def test__get_qual_ids__correct_string(self, mock_pattern):
        """Response -> get_qual_ids"""
        arguments = self.mock_arguments(self.CSV)
        mock_pattern.return_value = self.get_mock_pattern()

        response = Response(arguments)

        self.assertEqual(self.QUAL_IDS, response.get_qual_ids())

    def get_mock_pattern(self):
        mock = Mock()
        mock.random = Mock()
        mock.random.side_effect = TestResponse.QUAL_IDS
        return mock

    def mock_arguments(self, format_string):
        mock = Mock()
        mock.get_categories.return_value = self.CATEGORIES
        mock.get_group.return_value = self.GROUP
        mock.get_format.return_value = format_string
        mock.get_number.return_value = self.NUMBER
        mock.get_command.return_value = Command.MAIN
        return mock


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
