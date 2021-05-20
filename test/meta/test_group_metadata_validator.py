import unittest
from qual_id.groups.group import Group
from test.meta.group_metadata_validator import GroupMetadataValidator
from qual_id.categories.adjective import Adjective
from qual_id.categories.bird import Bird
from qual_id.categories.cake import Cake


class TestGroupMetadataValidator(unittest.TestCase):
    def test__validate__valid_group__empty_string(self):
        error_message = GroupMetadataValidator.validate(MockValidGroup)
        self.assertEqual(error_message, "")

    def test__validate__invalid_group_due_to_no_name__correct_error(self):
        self.validate_group(MockInvalidGroup_NoName)

    def test__validate__invalid_group_due_to_uppercase_name__correct_error(self):
        self.validate_group(MockInvalidGroup_UppercaseName)

    def test__validate__invalid_group_due_to_empty_list__correct_error(self):
        self.validate_group(MockInvalidGroup_Empty)

    def test__validate__invalid_group_due_to_repeats__correct_error(self):
        self.validate_group(MockInvalidGroup_Repeats)

    def test__validate__invalid_group_due_to_non_alphabetical__correct_error(self):
        self.validate_group(MockInvalidGroup_NonAlphabetical)

    def test__validate__invalid_group_due_to_containing_a_non_group__correct_error(self):
        self.validate_group(MockInvalidGroup_Nongroup)

    def validate_group(self, group):
        error_message = GroupMetadataValidator.validate(group)
        self.assertEqual(error_message, group.EXPECTED_ERROR_MESSAGE)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()


class MockValidGroup(Group):
    _name = "group"
    _categories = [Adjective, Bird, Cake]


class MockInvalidGroup_NoName(Group):
    _name = ""
    _categories = [Adjective, Bird, Cake]
    EXPECTED_ERROR_MESSAGE = "should have a name"


class MockInvalidGroup_UppercaseName(Group):
    _name = "UppercaseName"
    _categories = [Adjective, Bird, Cake]
    EXPECTED_ERROR_MESSAGE = "name should be all lowercase"


class MockInvalidGroup_Empty(Group):
    _name = "empty"
    _categories = []
    EXPECTED_ERROR_MESSAGE = "should return non-empty list"


class MockInvalidGroup_Repeats(Group):
    _name = "repeats"
    _categories = [Adjective, Bird, Bird]
    EXPECTED_ERROR_MESSAGE = "contains repeats: " + Bird.name()


class MockInvalidGroup_NonAlphabetical(Group):
    _name = "nonalphabetical"
    _categories = [Bird, Adjective, Cake]
    EXPECTED_ERROR_MESSAGE = "should be in alphabetical order"


class NongroupClass:
        @classmethod
        def name(cls):
            return "nongroupclass"

class MockInvalidGroup_Nongroup(Group):
    _name = "nongroup"
    _categories = [Adjective, Bird, NongroupClass]
    EXPECTED_ERROR_MESSAGE = "contains invalid class: " + str(NongroupClass)
