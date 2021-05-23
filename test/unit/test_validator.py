import unittest
from qual_id.validator import Validator


class TestValidator(unittest.TestCase):
    """Unit Tests for Validator"""

    VALID_GROUP = "all"
    VALID_CATEGORIES = ["fruit", "geography"]
    VALID_NUMBER = "3"
    VALID_FORMAT = "json"
    INVALID_GROUP = "invalid-group"
    INVALID_CATEGORIES = ["invalid-1", "invalid-2"]
    INVALID_NUMBER = "1.5"
    INVALID_FORMAT = "invalid-format"

    def test_validate__valid_arguments__none(self):
        """Validator -> validate - valid arguments"""
        result = Validator.validate(
            self.VALID_GROUP,
            self.VALID_CATEGORIES,
            self.VALID_NUMBER,
            self.VALID_FORMAT,
        )
        self.assertEqual(None, result)

    def test_validate__invalid_group__correct_error_message(self):
        """Validator -> validate - invalid group"""
        result = Validator.validate(
            self.INVALID_GROUP,
            self.VALID_CATEGORIES,
            self.VALID_NUMBER,
            self.VALID_FORMAT,
        )
        self.assertEqual(self._get_group_error_message(), result)

    def test_validate__invalid_categories__correct_error_message(self):
        """Validator -> validate - invalid categories"""
        invalid_categories = [*self.VALID_CATEGORIES, *self.INVALID_CATEGORIES]
        result = Validator.validate(
            self.VALID_GROUP, invalid_categories, self.VALID_NUMBER, self.VALID_FORMAT
        )
        self.assertEqual(self._get_categories_error_message(), result)

    def test_validate__invalid_number__correct_error_message(self):
        """Validator -> validate - invalid number"""
        result = Validator.validate(
            self.VALID_GROUP,
            self.VALID_CATEGORIES,
            self.INVALID_NUMBER,
            self.VALID_FORMAT,
        )
        self.assertEqual(self._get_number_error_message(), result)

    def test_validate__invalid_format__correct_error_message(self):
        """Validator -> validate - invalid format"""
        result = Validator.validate(
            self.VALID_GROUP,
            self.VALID_CATEGORIES,
            self.VALID_NUMBER,
            self.INVALID_FORMAT,
        )
        self.assertEqual(self._get_format_error_message(), result)

    def test_validate__invalid_group_and_categories__group_error_message(self):
        """Validator -> validate - invalid group"""
        result = Validator.validate(
            self.INVALID_GROUP,
            self.INVALID_CATEGORIES,
            self.VALID_NUMBER,
            self.INVALID_FORMAT,
        )
        self.assertEqual(self._get_group_error_message(), result)

    def _get_group_error_message(self):
        return "Group '{0}' does not exist.".format(self.INVALID_GROUP)

    def _get_categories_error_message(self):
        return "Categories do not exist: '{0}'.".format(
            ", ".join(self.INVALID_CATEGORIES)
        )

    def _get_number_error_message(self):
        return "Number argument is not an integer."

    def _get_format_error_message(self):
        return "Format must be 'json' or 'csv'."
