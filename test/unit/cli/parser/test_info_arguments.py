import unittest
from argparse import Namespace
from qual_id.cli.parser import Command
from qual_id.info.flag import Flag
from qual_id.cli.parser.info_arguments import InfoArguments
from unittest.mock import patch, Mock


class TestInfoArguments(unittest.TestCase):
    """Unit Tests for InfoArguments"""

    GROUP = "all"
    CATEGORY = "fruit"
    FORMAT = "json"

    def test__get_flag__group_None__correct_flag(self):
        """InfoArguments -> get_flag - group None"""
        namespace = self.get_namespace(group=None)
        arguments = InfoArguments(namespace)
        self.assertEqual(Flag.GROUP, arguments.get_flag())

    def test__get_flag__group_value__correct_flag(self):
        """InfoArguments -> get_flag - group value"""
        namespace = self.get_namespace(group=self.GROUP)
        arguments = InfoArguments(namespace)
        self.assertEqual(Flag.GROUP, arguments.get_flag())

    def test__get_flag__category_None__correct_flag(self):
        """InfoArguments -> get_flag - category None"""
        namespace = self.get_namespace(category=None)
        arguments = InfoArguments(namespace)
        self.assertEqual(Flag.CATEGORY, arguments.get_flag())

    def test__get_flag__category_value__correct_flag(self):
        """InfoArguments -> get_flag - category value"""
        namespace = self.get_namespace(category=self.CATEGORY)
        arguments = InfoArguments(namespace)
        self.assertEqual(Flag.CATEGORY, arguments.get_flag())

    def test__get_flag__format_true__correct_flag(self):
        """InfoArguments -> get_flag - format true"""
        namespace = self.get_namespace(format=True)
        arguments = InfoArguments(namespace)
        self.assertEqual(Flag.FORMAT, arguments.get_flag())

    def test__get_value__group_None__correct_flag(self):
        """InfoArguments -> get_value - group None"""
        namespace = self.get_namespace(group=None)
        arguments = InfoArguments(namespace)
        self.assertEqual(None, arguments.get_value())

    def test__get_value__group_value__correct_flag(self):
        """InfoArguments -> get_value - group value"""
        namespace = self.get_namespace(group=self.GROUP)
        arguments = InfoArguments(namespace)
        self.assertEqual(self.GROUP, arguments.get_value())

    def test__get_value__category_None__correct_flag(self):
        """InfoArguments -> get_value - category None"""
        namespace = self.get_namespace(category=None)
        arguments = InfoArguments(namespace)
        self.assertEqual(None, arguments.get_value())

    def test__get_value__category_value__correct_flag(self):
        """InfoArguments -> get_value - category value"""
        namespace = self.get_namespace(category=self.CATEGORY)
        arguments = InfoArguments(namespace)
        self.assertEqual(self.CATEGORY, arguments.get_value())

    def test__get_value__format_true__correct_flag(self):
        """InfoArguments -> get_value - format true"""
        namespace = self.get_namespace(format=True)
        arguments = InfoArguments(namespace)
        self.assertEqual(None, arguments.get_value())

    def test__get_command__main(self):
        """InfoArguments -> get_command"""
        namespace = self.get_namespace()
        arguments = InfoArguments(namespace)
        self.assertEqual(Command.INFO, arguments.get_command())

    def get_namespace(self, group=False, category=False, format=None):
        return Namespace(group=group, category=category, format=format)
