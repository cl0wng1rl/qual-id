import unittest
from qual_id.validators.collection_validator import CollectionValidator
from qual_id.collections import CollectionFactory
from unittest.mock import patch


class TestCollectionValidator(unittest.TestCase):
    @patch.object(CollectionFactory, "has")
    def test__validate__valid_collection__is_valid_returns_true(
        self, mock_collection_factory_has
    ):
        mock_collection_factory_has.return_value = True
        validator = CollectionValidator("ValidCollectionName")
        validator.validate()
        self.assertTrue(validator.is_valid())

    @patch.object(CollectionFactory, "has")
    def test__validate__invalid_collection__is_valid_returns_false(
        self, mock_collection_factory_has
    ):
        mock_collection_factory_has.return_value = False
        validator = CollectionValidator("InvalidCollectionName")
        validator.validate()
        self.assertFalse(validator.is_valid())

    @patch.object(CollectionFactory, "has")
    def test__validate__invalid_collection__error_message_returns_correct_message(
        self, mock_collection_factory_has
    ):
        mock_collection_factory_has.return_value = False
        validator = CollectionValidator("InvalidCollectionName")
        validator.validate()
        expected_message = "invalid collection: InvalidCollectionName"
        self.assertEqual(expected_message, validator.error_message())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
