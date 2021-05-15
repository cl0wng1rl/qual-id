import unittest
from qual_id.collections import *
from test.meta.collection_metadata_validator import CollectionMetadataValidator


class TestCollections(unittest.TestCase):
    def setUp(self):
        self.collections = TestCollections._get_all_collections()

    def test__all_collections__values_are_valid(self):
        [self.validate_values_are_valid(collection) for collection in self.collections]

    def validate_values_are_valid(self, collection):
        error_message = CollectionMetadataValidator.validate(collection)
        self.assertTrue(
            error_message == "",
            TestCollections._user_error_message(collection, error_message),
        )

    @staticmethod
    def _user_error_message(collection, error_message):
        return "\n" + collection._name + ": \n" + error_message

    @staticmethod
    def _get_all_collections():
        return [
            All,
            Minimal,
            Neutral,
        ]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
