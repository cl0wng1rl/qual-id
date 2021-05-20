import unittest
from qual_id.cli.main.validator import Validator


class TestValidator(unittest.TestCase):
    COMMAND_NAME = "qid"
    PATTERN_FLAG = "--pattern"
    PATTERN = "category1-category2"
    FORMAT_FLAG = "--format"
    INVALID_FLAG = "--nonexistentflag"
    FORMAT = "format"

    def test__is_valid__valid_args__true(self):
        validator = Validator(self.get_valid_args())
        self.assertTrue(validator.is_valid())

    def test__error_message__valid_args__none(self):
        validator = Validator(self.get_valid_args())
        self.assertEqual(None, validator.error_message())

    def test__is_valid__flag_without_value__false(self):
        validator = Validator(self.get_invalid_args__no_pattern())
        self.assertFalse(validator.is_valid())

    def test__error_message__flag_without_value__correct_message(self):
        validator = Validator(self.get_invalid_args__no_pattern())
        expected_message = "no {0} specified".format(self.PATTERN_FLAG[2:])
        self.assertEqual(expected_message, validator.error_message())

    def test__is_valid__invalid_flag__false(self):
        validator = Validator(self.get_invalid_args__invalid_flag())
        self.assertFalse(validator.is_valid())

    def test__error_message__invalid_flag__correct_message(self):
        validator = Validator(self.get_invalid_args__invalid_flag())
        expected_message = "invalid flag: {0}".format(self.INVALID_FLAG)
        self.assertEqual(expected_message, validator.error_message())

    def get_valid_args(self):
        return [
            self.COMMAND_NAME,
            self.PATTERN_FLAG,
            self.PATTERN,
            self.FORMAT_FLAG,
            self.FORMAT,
        ]

    def get_invalid_args__no_pattern(self):
        return [self.COMMAND_NAME, self.PATTERN_FLAG]

    def get_invalid_args__invalid_flag(self):
        return [self.COMMAND_NAME, self.INVALID_FLAG]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
