import unittest
from qual_id.categories.category import Category
from test.meta.category_metadata_validator import CategoryMetadataValidator


class TestCategoryMetadataValidator(unittest.TestCase):
    def test__validate__with_valid_category__empty_string(self):
        error_message = CategoryMetadataValidator.validate(MockValidCategory)
        self.assertEqual(error_message, "")

    def test__validate__invalid_category_due_to_no_name__correct_error(self):
        self.validate_category(MockInvalidCategory_NoName)

    def test__validate__invalid_category_due_to_uppercase_name__correct_error(self):
        self.validate_category(MockInvalidCategory_UppercaseName)

    def test__validate__invalid_category_due_to_spaces__correct_error(self):
        self.validate_category(MockInvalidCategory_Spaces)

    def test__validate__invalid_category_due_to_dashes__correct_error(self):
        self.validate_category(MockInvalidCategory_Dashes)

    def test__validate__invalid_category_due_to_empty_list__correct_error(self):
        self.validate_category(MockInvalidCategory_Empty)

    def test__validate__invalid_category_due_to_repeats__correct_error(self):
        self.validate_category(MockInvalidCategory_Repeats)

    def test__validate__invalid_category_due_to_non_alphabetical__correct_error(self):
        self.validate_category(MockInvalidCategory_NonAlphabetical)

    def test__validate__invalid_category_due_to_uppercase__correct_error(self):
        self.validate_category(MockInvalidCategory_Uppercase)

    def validate_category(self, category):
        error_message = CategoryMetadataValidator.validate(category)
        self.assertEqual(error_message, category.EXPECTED_ERROR_MESSAGE)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()


class MockValidCategory(Category):
    _name = "category"
    _values = ["valuea", "valueb", "valuec"]


class MockInvalidCategory_NoName(Category):
    _name = ""
    _values = ["valuea", "valueb", "valuec"]
    EXPECTED_ERROR_MESSAGE = "should have a name"


class MockInvalidCategory_UppercaseName(Category):
    _name = "UppercaseName"
    _values = ["valuea", "valueb", "valuec"]
    EXPECTED_ERROR_MESSAGE = "name should be all lowercase"


class MockInvalidCategory_Spaces(Category):
    _name = "spaces"
    _values = ["value a", "value b", "value c"]
    EXPECTED_ERROR_MESSAGE = "contains invalid strings: value a, value b, value c"


class MockInvalidCategory_Dashes(Category):
    _name = "dashes"
    _values = ["value-a", "value-b", "value-c"]
    EXPECTED_ERROR_MESSAGE = "contains invalid strings: value-a, value-b, value-c"


class MockInvalidCategory_Empty(Category):
    _name = "empty"
    _values = []
    EXPECTED_ERROR_MESSAGE = "should return non-empty list"


class MockInvalidCategory_Repeats(Category):
    _name = "repeats"
    _values = ["valuea", "valueb", "valueb"]
    EXPECTED_ERROR_MESSAGE = "contains repeats: valueb"


class MockInvalidCategory_NonAlphabetical(Category):
    _name = "nonalphabetical"
    _values = ["valuec", "valuea", "valueb"]
    EXPECTED_ERROR_MESSAGE = "should be in alphabetical order"


class MockInvalidCategory_Uppercase(Category):
    _name = "uppercase"
    _values = ["valueA", "valueB", "valueC"]
    EXPECTED_ERROR_MESSAGE = "contains uppercase strings: valueA, valueB, valueC"
