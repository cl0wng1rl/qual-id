import unittest
from qual_id.validators import FormatValidator


class TestFormatValidator(unittest.TestCase):
    VALID_FORMATS = ["json", "csv"]

    def test__validate__json_string__is_valid_returns_true(self):
        validator = FormatValidator("json")
        validator.validate()
        self.assertTrue(validator.is_valid())

    def test__validate__csv_string__is_valid_returns_true(self):
        validator = FormatValidator("csv")
        validator.validate()
        self.assertTrue(validator.is_valid())

    def test__validate__invalid_string__is_valid_returns_false(self):
        validator = FormatValidator("invalid string")
        validator.validate()
        self.assertFalse(validator.is_valid())

    def test__validate__invalid_string__error_message_returns_correct_message(self):
        validator = FormatValidator("6")
        validator.validate()
        expected_message = "'format' argument must be " + self.join_valid_formats()
        self.assertEqual(expected_message, validator.error_message())

    def join_valid_formats(self):
        return " or ".join([", ".join(self.VALID_FORMATS[:-1]), self.VALID_FORMATS[-1]])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
