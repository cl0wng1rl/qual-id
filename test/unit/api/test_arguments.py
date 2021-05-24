import unittest
from qual_id.api.arguments import Arguments
from unittest.mock import patch, Mock


class TestArguments(unittest.TestCase):
    """Unit Tests for Arguments"""

    GROUP = "all"
    CATEGORIES = ["fruit", "geography"]
    MOCK_CATEGORIES = [ Mock(), Mock() ]
    NUMBER = "3"
    FORMAT = "json"
    ARGS = {
        "group": GROUP,
        "categories": CATEGORIES,
        "number": NUMBER,
        "format": FORMAT
    }

    @patch("qual_id.api.arguments.GroupFactory")
    def test__get_group__correct_group(self, mock_group_factory):
        """Arguments -> get_group"""
        group = self.get_mock_group()
        mock_group_factory.get.return_value = group
        arguments = Arguments(self.ARGS)
        self.assertEqual(group, arguments.get_group())

    @patch("qual_id.api.arguments.GroupFactory")
    def test__get_categories__correct_categories(self, mock_group_factory):
        """Arguments -> get_categories"""
        mock_group_factory.get.return_value = self.get_mock_group()
        arguments = Arguments(self.ARGS)
        self.assertEqual(self.MOCK_CATEGORIES, arguments.get_categories())

    @patch("qual_id.api.arguments.GroupFactory")
    def test__get_number__correct_number(self, mock_group_factory):
        """Arguments -> get_number"""
        mock_group_factory.get.return_value = self.get_mock_group()
        arguments = Arguments(self.ARGS)
        self.assertEqual(int(self.NUMBER), arguments.get_number())

    @patch("qual_id.api.arguments.GroupFactory")
    def test__get_format__correct_format(self, mock_group_factory):
        """Arguments -> get_format"""
        mock_group_factory.get.return_value = self.get_mock_group()
        arguments = Arguments(self.ARGS)
        self.assertEqual(self.FORMAT, arguments.get_format())

    def get_mock_group(self):
        mock = Mock()
        mock.get.side_effect = self.MOCK_CATEGORIES
        return mock
