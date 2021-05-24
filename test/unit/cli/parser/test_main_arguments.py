import unittest
from argparse import Namespace
from qual_id.cli.parser import Command
from qual_id.cli.parser.main_arguments import MainArguments
from unittest.mock import patch, Mock


class TestMainArguments(unittest.TestCase):
    """Unit Tests for MainArguments"""

    GROUP = "all"
    CATEGORIES = ["fruit", "geography"]
    MOCK_CATEGORIES = [Mock(), Mock()]
    NUMBER = 3
    FORMAT = "json"
    NAMESPACE = Namespace(
        group=GROUP, categories=CATEGORIES, number=NUMBER, format=FORMAT
    )

    @patch("qual_id.cli.parser.main_arguments.GroupFactory")
    def test__get_group__correct_group(self, mock_group_factory):
        """MainArguments -> get_group"""
        group = self.get_mock_group()
        mock_group_factory.get.return_value = group
        arguments = MainArguments(self.NAMESPACE)
        self.assertEqual(group, arguments.get_group())

    @patch("qual_id.cli.parser.main_arguments.GroupFactory")
    def test__get_categories__correct_categories(self, mock_group_factory):
        """MainArguments -> get_categories"""
        mock_group_factory.get.return_value = self.get_mock_group()
        arguments = MainArguments(self.NAMESPACE)
        self.assertEqual(self.MOCK_CATEGORIES, arguments.get_categories())

    @patch("qual_id.cli.parser.main_arguments.GroupFactory")
    def test__get_number__correct_number(self, mock_group_factory):
        """MainArguments -> get_number"""
        mock_group_factory.get.return_value = self.get_mock_group()
        arguments = MainArguments(self.NAMESPACE)
        self.assertEqual(int(self.NUMBER), arguments.get_number())

    @patch("qual_id.cli.parser.main_arguments.GroupFactory")
    def test__get_format__correct_format(self, mock_group_factory):
        """MainArguments -> get_format"""
        mock_group_factory.get.return_value = self.get_mock_group()
        arguments = MainArguments(self.NAMESPACE)
        self.assertEqual(self.FORMAT, arguments.get_format())

    @patch("qual_id.cli.parser.main_arguments.GroupFactory")
    def test__get_command__main(self, mock_group_factory):
        """MainArguments -> get_command"""
        mock_group_factory.get.return_value = self.get_mock_group()
        arguments = MainArguments(self.NAMESPACE)
        self.assertEqual(Command.MAIN, arguments.get_command())

    def get_mock_group(self):
        mock = Mock()
        mock.get.side_effect = self.MOCK_CATEGORIES
        return mock
