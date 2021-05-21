import unittest
from qual_id.validators.format_validator import FormatValidator


class TestFormatValidator(unittest.TestCase):
    """Unit Tests for FormatValidator"""

    VALID_FORMATS = ["json", "csv"]

    def test__validate__json_string__true(self):
        """FormatValidator -> validate - json string"""
        validator = FormatValidator("json")
        validator.validate()
        self.assertTrue(validator.is_valid())

    def test__validate__csv_string__true(self):
        """FormatValidator -> validate - csv string"""
        validator = FormatValidator("csv")
        validator.validate()
        self.assertTrue(validator.is_valid())

    def test__validate__invalid_string__false(self):
        """FormatValidator -> validate - invalid string"""
        validator = FormatValidator("invalid string")
        validator.validate()
        self.assertFalse(validator.is_valid())

    def test__error_message__invalid_string__correct_message(self):
        """FormatValidator -> error_message - invalid string"""
        validator = FormatValidator("6")
        validator.validate()
        expected_message = "'format' argument must be " + self.join_valid_formats()
        self.assertEqual(expected_message, validator.error_message())

    def join_valid_formats(self):
        return " or ".join([", ".join(self.VALID_FORMATS[:-1]), self.VALID_FORMATS[-1]])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
