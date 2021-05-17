import unittest
from qual_id.cli.validator import Validator


class TestValidator(unittest.TestCase):
    COMMAND_NAME = "qid"
    PATTERN_FLAG = "--pattern"
    PATTERN = "category1-category2"
    FORMAT_FLAG = "--format"
    HELP_FLAG = "--help"
    INVALID_FLAG = "--nonexistentflag"
    FORMAT = "format"

    def test__is_valid__valid_args__true(self):
        validator = Validator(self.get_valid_args())
        self.assertTrue(validator.is_valid())

    def test__is_help__valid_args__false(self):
        validator = Validator(self.get_valid_args())
        self.assertFalse(validator.is_help())

    def test__error_message__valid_args__none(self):
        validator = Validator(self.get_valid_args())
        self.assertEqual(None, validator.error_message())

    def test__is_valid__flag_without_value__false(self):
        validator = Validator(self.get_invalid_args__no_pattern())
        self.assertFalse(validator.is_valid())

    def test__is_help__flag_without_value__false(self):
        validator = Validator(self.get_invalid_args__no_pattern())
        self.assertFalse(validator.is_help())

    def test__error_message__flag_without_value__correct_message(self):
        validator = Validator(self.get_invalid_args__no_pattern())
        expected_message = "no {0} specified".format(self.PATTERN_FLAG[2:])
        self.assertEqual(expected_message, validator.error_message())

    def test__is_valid__invalid_flag__false(self):
        validator = Validator(self.get_invalid_args__invalid_flag())
        self.assertFalse(validator.is_valid())

    def test__is_help__invalid_flag__false(self):
        validator = Validator(self.get_invalid_args__invalid_flag())
        self.assertFalse(validator.is_help())

    def test__error_message__invalid_flag__correct_message(self):
        validator = Validator(self.get_invalid_args__invalid_flag())
        expected_message = "invalid flag: {0}".format(self.INVALID_FLAG)
        self.assertEqual(expected_message, validator.error_message())

    def test__is_valid__help_flag__true(self):
        validator = Validator(self.get_valid_args__help())
        self.assertTrue(validator.is_valid())

    def test__is_help__help_flag__true(self):
        validator = Validator(self.get_valid_args__help())
        self.assertTrue(validator.is_help())

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
    
    def get_valid_args__help(self):
        return [self.COMMAND_NAME, self.PATTERN, self.HELP_FLAG, self.FORMAT]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
