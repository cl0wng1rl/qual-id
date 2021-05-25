import unittest
from qual_id.groups.all import All
from qual_id.categories import *
from test.meta.category_metadata_validator import CategoryMetadataValidator


class TestCategories(unittest.TestCase):
    """Metadata Tests for Categories"""

    def setUp(self):
        self.categories = TestCategories._get_all_categories()

    def test__all_categories__values_are_valid(self):
        """Categories Metadata"""
        [self.validate_values_are_valid(category) for category in self.categories]

    def validate_values_are_valid(self, category):
        error_message = CategoryMetadataValidator.validate(category)
        self.assertTrue(
            error_message == "",
            TestCategories._user_error_message(category, error_message),
        )

    @staticmethod
    def _user_error_message(category, error_message):
        return "\n" + category._name + ": \n" + error_message

    @staticmethod
    def _get_all_categories():
        return All._categories


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
