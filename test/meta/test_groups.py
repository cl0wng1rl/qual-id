import unittest
from qual_id.groups.all import All
from qual_id.groups.minimal import Minimal
from qual_id.groups.neutral import Neutral
from test.meta.group_metadata_validator import GroupMetadataValidator


class TestGroups(unittest.TestCase):
    def setUp(self):
        self.groups = TestGroups._get_all_groups()

    def test__all_groups__values_are_valid(self):
        [self.validate_values_are_valid(group) for group in self.groups]

    def validate_values_are_valid(self, group):
        error_message = GroupMetadataValidator.validate(group)
        self.assertTrue(
            error_message == "",
            TestGroups._user_error_message(group, error_message),
        )

    @staticmethod
    def _user_error_message(group, error_message):
        return "\n" + group._name + ": \n" + error_message

    @staticmethod
    def _get_all_groups():
        return [
            All,
            Minimal,
            Neutral,
        ]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
