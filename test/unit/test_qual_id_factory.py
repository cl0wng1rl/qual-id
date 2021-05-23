import unittest
from qual_id.pattern import Pattern
from qual_id.parser.command import Command
from qual_id.qual_id_factory import QualIDFactory
from unittest.mock import Mock, call, patch


class TestQualIDFactory(unittest.TestCase):
    """Unit Tests for QualIDFactory"""

    CSV = "csv"
    JSON = "json"
    QUAL_IDS = ["qual_id1", "qual_id2", "qual_id3"]
    CATEGORIES = ["category1", "category2"]
    GROUP = "all"
    NUMBER = 3

    @patch("qual_id.qual_id_factory.Pattern")
    def test__get_qual_ids__correct_list_of_qual_ids(self, mock_pattern):
        """QualIDFactory -> get_qual_ids"""
        arguments = self.mock_arguments(self.CSV)
        mock_pattern.return_value = self.get_mock_pattern()

        qual_ids = QualIDFactory.get_qual_ids(arguments)

        self.assertEqual(self.QUAL_IDS, qual_ids)

    def get_mock_pattern(self):
        mock = Mock()
        mock.random = Mock()
        mock.random.side_effect = self.QUAL_IDS
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
