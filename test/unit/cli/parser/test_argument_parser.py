import unittest
from argparse import Namespace
from qual_id.cli.parser.argument_parser import ArgumentParser
from qual_id.cli.parser.main_arguments import MainArguments
from unittest.mock import patch, Mock


class TestArgumentParser(unittest.TestCase):
    """Unit Tests for ArgumentParser"""

    ARGS = ["arg1", "arg2", "arg3"]

    @patch("qual_id.cli.parser.argument_parser.ArgParser")
    def test__parse__calls_parse_args(self, mock_arg_parser):
        """ArgumentParser -> parse - arguments - calls 'parse_args'"""
        mock_parser = self.get_mock_parser()
        mock_arg_parser.return_value = mock_parser
        result = ArgumentParser().parse(self.ARGS)
        mock_parser.parse_args.assert_called_with(self.ARGS)

    def get_mock_parser(self):
        mock = Mock()
        mock.add_subparsers.return_value = Mock()
        mock.add_subparsers.return_value.add_parser.return_value = Mock()
        return mock
