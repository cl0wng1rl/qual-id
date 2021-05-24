import unittest
from argparse import ArgumentError, ArgumentTypeError
from qual_id.cli.parser.argument_parser import ArgumentParser
import random


class TestArgumentParser_Integration(unittest.TestCase):
    """Integration Tests for ArgumentParser module"""

    def test__parse__too_many_categories__expected_error(self):
        """ArgumentParser -> parse - too many categories"""
        self.assert_scenario(TooManyCategoriesScenario())

    def test__parse__no_value_after_group_flag__expected_error(self):
        """ArgumentParser -> parse - no value after group flag"""
        self.assert_scenario(NoGroupScenario())

    def test__parse__no_value_after_categories_flag__expected_error(self):
        """ArgumentParser -> parse - no value after categories flag"""
        self.assert_scenario(NoCategoriesScenario())

    def test__parse__no_value_after_format_flag__expected_error(self):
        """ArgumentParser -> parse - no value after format flag"""
        self.assert_scenario(NoFormatScenario())

    def test__parse__no_value_after_number_flag__expected_error(self):
        """ArgumentParser -> parse - no value after number flag"""
        self.assert_scenario(NoNumberScenario())

    def test__parse__invalid_group_value__expected_error(self):
        """ArgumentParser -> parse - invalid group value"""
        self.assert_scenario(InvalidGroupScenario())

    def test__parse__invalid_categories_value__expected_error(self):
        """ArgumentParser -> parse - invalid categories value"""
        self.assert_scenario_includes(InvalidCategoriesScenario())

    def test__parse__invalid_format_value__expected_error(self):
        """ArgumentParser -> parse - invalid format value"""
        self.assert_scenario(InvalidFormatScenario())

    def test__parse__invalid_number_value__expected_error(self):
        """ArgumentParser -> parse - invalid number value"""
        self.assert_scenario(InvalidNumberScenario())

    def assert_scenario(self, scenario):
        parser = self.get_parser()
        try:
            parser.parse(scenario.arguments())
        except Exception as err:
            self.assertEqual(scenario.expected(), err.args[0])

    def assert_scenario_includes(self, scenario):
        parser = self.get_parser()
        try:
            parser.parse(scenario.arguments())
        except Exception as err:
            self.assertTrue(scenario.expected() in err.args[0])

    def get_parser(self):
        parser = ArgumentParser()
        # Suppress exiting method and displaying usage info
        parser._parser.exit = self.error_handler
        parser._parser.print_usage = self.print_usage
        return parser

    def error_handler(self, status=0, message=None):
        if status:
            raise Exception(message)

    def print_usage(self, file=None):
        pass


class Scenario:
    CATEGORIES_FLAG = "--categories"
    CATEGORIES = ["fruit", "geography"]
    INVALID_CATEGORIES = ["fruit", "invalid"]
    GROUP_FLAG = "--group"
    GROUP = "all"
    INVALID_GROUP = "invalid"
    FORMAT_FLAG = "--format"
    FORMAT_CSV = "csv"
    INVALID_FORMAT = "invalid"
    NUMBER_FLAG = "--number"
    NUMBER = "3"
    INVALID_NUMBER = "invalid"

    @classmethod
    def arguments(cls):
        return cls._arguments

    @classmethod
    def expected(cls):
        return cls._expected


class TooManyCategoriesScenario(Scenario):
    _arguments = [
        Scenario.CATEGORIES_FLAG,
        *(Scenario.CATEGORIES * 3),
        Scenario.GROUP_FLAG,
        Scenario.FORMAT_FLAG,
        Scenario.FORMAT_CSV,
        Scenario.NUMBER_FLAG,
        Scenario.NUMBER,
    ]
    _expected = 'qid: error: argument "categories" requires between 1 and 5 arguments\n'


class NoGroupScenario(Scenario):
    _arguments = [Scenario.CATEGORIES_FLAG, *Scenario.CATEGORIES, Scenario.GROUP_FLAG]
    _expected = "qid: error: argument -g/--group: expected one argument\n"


class NoCategoriesScenario(Scenario):
    _arguments = [Scenario.CATEGORIES_FLAG]
    _expected = "qid: error: argument -c/--categories: expected at least one argument\n"


class NoFormatScenario(Scenario):
    _arguments = [Scenario.CATEGORIES_FLAG, *Scenario.CATEGORIES, Scenario.FORMAT_FLAG]
    _expected = "qid: error: argument -f/--format: expected one argument\n"


class NoNumberScenario(Scenario):
    _arguments = [Scenario.CATEGORIES_FLAG, *Scenario.CATEGORIES, Scenario.NUMBER_FLAG]
    _expected = "qid: error: argument -n/--number: expected one argument\n"


class InvalidGroupScenario(Scenario):
    _arguments = [
        Scenario.CATEGORIES_FLAG,
        *Scenario.CATEGORIES,
        Scenario.GROUP_FLAG,
        Scenario.INVALID_GROUP,
    ]
    _expected = "qid: error: argument -g/--group: invalid choice: '{0}' (choose from 'all', 'minimal', 'neutral')\n".format(
        Scenario.INVALID_GROUP
    )


class InvalidCategoriesScenario(Scenario):
    _arguments = [Scenario.CATEGORIES_FLAG, *Scenario.INVALID_CATEGORIES]
    _expected = (
        "qid: error: argument -c/--categories: invalid choice: 'invalid' (choose from "
    )


class InvalidFormatScenario(Scenario):
    _arguments = [
        Scenario.CATEGORIES_FLAG,
        *Scenario.CATEGORIES,
        Scenario.FORMAT_FLAG,
        Scenario.INVALID_FORMAT,
    ]
    _expected = "qid: error: argument -f/--format: invalid choice: '{0}' (choose from 'csv', 'json')\n".format(
        Scenario.INVALID_FORMAT
    )


class InvalidNumberScenario(Scenario):
    _arguments = [
        Scenario.CATEGORIES_FLAG,
        *Scenario.CATEGORIES,
        Scenario.NUMBER_FLAG,
        Scenario.INVALID_NUMBER,
    ]
    _expected = "qid: error: argument -n/--number: invalid int value: '{0}'\n".format(
        Scenario.INVALID_NUMBER
    )
