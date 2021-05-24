import unittest
from argparse import Namespace
from qual_id.cli.parser import Command
from qual_id.cli.parser.main_arguments import MainArguments
from qual_id.cli.parser.info_arguments import InfoArguments
from qual_id.cli.parser import Parser
from unittest.mock import patch, Mock


class TestParser(unittest.TestCase):
    """Unit Tests for Parser"""

    ARGUMENTS = ["arg1", "arg2", "arg3"]

    @patch("qual_id.cli.parser.parser.MainArguments")
    @patch("qual_id.cli.parser.parser.InfoArguments")
    @patch("qual_id.cli.parser.parser.ArgumentParser")
    def test__parse__main_command_namespace__correct_aruments_type(self, mock_parser, mock_info_args, mock_main_args):
        """Parser -> parse - main command namespace"""
        main_mock = Mock()
        mock_main_args.return_value = main_mock
        namespace = self.get_mock_namespace(Command.MAIN)
        self.set_mock_parser(mock_parser, namespace)
        result = Parser.parse(self.ARGUMENTS)
        self.assertEqual(main_mock, result)
        mock_main_args.assert_called_with(namespace)

    @patch("qual_id.cli.parser.parser.MainArguments")
    @patch("qual_id.cli.parser.parser.InfoArguments")
    @patch("qual_id.cli.parser.parser.ArgumentParser")
    def test__parse__info_command_namespace__correct_aruments_type(self, mock_parser, mock_info_args, mock_main_args):
        """Parser -> parse - info command namespace"""
        info_mock = Mock()
        mock_info_args.return_value = info_mock
        namespace = self.get_mock_namespace(Command.INFO)
        self.set_mock_parser(mock_parser, namespace)
        result = Parser.parse(self.ARGUMENTS)
        self.assertEqual(info_mock, result)
        mock_info_args.assert_called_with(namespace)

    def get_mock_namespace(self, command):
        mock = Mock()
        mock.command = command
        return mock
    
    def set_mock_parser(self, parser, namespace):
        parser.return_value.parse.return_value = namespace
