import unittest
from qual_id.cli.helper import Helper



class TestHelper(unittest.TestCase):
    HELP_LONG = "--help"
    HELP_SHORT = "-h"
    HELP_MESSAGE_LINES = ["line1", "line2", "line3"]

    def test__is_help__with_long_help_flag__true(self):
        helper = MockHelper(["arg1", self.HELP_LONG, "arg2"])
        self.assertTrue(helper.is_help())

    def test__is_help__with_short_help_flag__true(self):
        helper = MockHelper(["arg1", self.HELP_SHORT, "arg2"])
        self.assertTrue(helper.is_help())

    def test__is_help__without_help_flag__false(self):
        helper = MockHelper(["arg1", "arg2", "arg3"])
        self.assertFalse(helper.is_help())

    def test__help_message__correct_message(self):
        helper = MockHelper(["arg1", self.HELP_LONG, "arg2"])
        expected_message = "\n".join(self.HELP_MESSAGE_LINES)
        self.assertEqual(expected_message, helper.help_message())

class MockHelper(Helper):
    HELP_MESSAGE_LINES = TestHelper.HELP_MESSAGE_LINES


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
