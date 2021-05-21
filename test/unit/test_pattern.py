import unittest
import random
from qual_id.pattern import Pattern
from unittest.mock import Mock, call, patch


class TestPattern(unittest.TestCase):
    """Unit Tests for Pattern"""

    CATEGORY_KEYS = ["first_category", "second_category"]
    CATEGORY_VALUES = ["first_category_value", "second_category_value"]
    PATTERN = "-".join(CATEGORY_KEYS[:2])

    def test__random__pattern__correct_qual_id(self):
        """Pattern -> random"""
        category_names = TestPattern.CATEGORY_KEYS
        mock_group = self.get_mock_group()
        pattern = Pattern(category_names, mock_group)

        result = pattern.random()

        self.assertEqual("-".join([self.CATEGORY_VALUES[0]] * 2), result)

    def test__init__pattern__correctly_calls_get_on_group(self):
        """Pattern -> __init__ - calls get on group"""
        category_names = TestPattern.CATEGORY_KEYS
        mock_group = self.get_mock_group()

        pattern = Pattern(category_names, mock_group)

        expected_calls = [call(self.CATEGORY_KEYS[0]), call(self.CATEGORY_KEYS[1])]
        self.assertEqual(expected_calls, mock_group.get.call_args_list)

    def get_mock_group(self):
        mock = Mock()
        mock.get.return_value = self.mock_category()
        mock.invalid.return_value = []
        return mock

    def mock_category(self):
        mock = Mock()
        mock.name.return_value = self.CATEGORY_KEYS[0]
        mock.random.return_value = self.CATEGORY_VALUES[0]
        return mock


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
