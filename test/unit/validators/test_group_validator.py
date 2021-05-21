import unittest
from qual_id.validators.group_validator import GroupValidator
from qual_id.groups import GroupFactory
from unittest.mock import patch


class TestGroupValidator(unittest.TestCase):
    """Unit Tests for GroupValidator"""

    @patch.object(GroupFactory, "has")
    def test__validate__valid_group__true(
        self, mock_group_factory_has
    ):
        """GroupValidator -> validate - valid group"""
        mock_group_factory_has.return_value = True
        validator = GroupValidator("ValidGroupName")
        validator.validate()
        self.assertTrue(validator.is_valid())

    @patch.object(GroupFactory, "has")
    def test__validate__invalid_group__false(
        self, mock_group_factory_has
    ):
        """GroupValidator -> validate - invalid group"""
        mock_group_factory_has.return_value = False
        validator = GroupValidator("InvalidGroupName")
        validator.validate()
        self.assertFalse(validator.is_valid())

    @patch.object(GroupFactory, "has")
    def test__error_message__invalid_group__correct_message(
        self, mock_group_factory_has
    ):
        """GroupValidator -> error_message - invalid group"""
        mock_group_factory_has.return_value = False
        validator = GroupValidator("InvalidGroupName")
        validator.validate()
        expected_message = "invalid group: InvalidGroupName"
        self.assertEqual(expected_message, validator.error_message())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
