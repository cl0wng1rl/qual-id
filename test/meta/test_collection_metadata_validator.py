import unittest
from qual_id.collection import Collection
from test.meta.collection_metadata_validator import CollectionMetadataValidator
from qual_id.categories.adjective import Adjective
from qual_id.categories.bird import Bird
from qual_id.categories.cake import Cake


class TestCollectionMetadataValidator(unittest.TestCase):
    def test__validate__with_valid_collection__returns_empty_string(self):
        error_message = CollectionMetadataValidator.validate(MockValidCollection)
        self.assertEqual(error_message, "")

    def test__validate__invalid_collection_due_to_no_name__correct_error(self):
        self.validate_collection(MockInvalidCollection_NoName)

    def test__validate__invalid_collection_due_to_uppercase_name__correct_error(self):
        self.validate_collection(MockInvalidCollection_UppercaseName)

    def test__validate__invalid_collection_due_to_empty_list__correct_error(self):
        self.validate_collection(MockInvalidCollection_Empty)

    def test__validate__invalid_collection_due_to_repeats__correct_error(self):
        self.validate_collection(MockInvalidCollection_Repeats)

    def test__validate__invalid_collection_due_to_non_alphabetical__correct_error(self):
        self.validate_collection(MockInvalidCollection_NonAlphabetical)

    def test__validate__invalid_collection_due_to_containing_a_non_collection__correct_error(self):
        self.validate_collection(MockInvalidCollection_Noncollection)

    def validate_collection(self, collection):
        error_message = CollectionMetadataValidator.validate(collection)
        self.assertEqual(error_message, collection.EXPECTED_ERROR_MESSAGE)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()


class MockValidCollection(Collection):
    _name = "collection"
    _categories = [Adjective, Bird, Cake]


class MockInvalidCollection_NoName(Collection):
    _name = ""
    _categories = [Adjective, Bird, Cake]
    EXPECTED_ERROR_MESSAGE = "should have a name"


class MockInvalidCollection_UppercaseName(Collection):
    _name = "UppercaseName"
    _categories = [Adjective, Bird, Cake]
    EXPECTED_ERROR_MESSAGE = "name should be all lowercase"


class MockInvalidCollection_Empty(Collection):
    _name = "empty"
    _categories = []
    EXPECTED_ERROR_MESSAGE = "should return non-empty list"


class MockInvalidCollection_Repeats(Collection):
    _name = "repeats"
    _categories = [Adjective, Bird, Bird]
    EXPECTED_ERROR_MESSAGE = "contains repeats: " + str(Bird)


class MockInvalidCollection_NonAlphabetical(Collection):
    _name = "nonalphabetical"
    _categories = [Bird, Adjective, Cake]
    EXPECTED_ERROR_MESSAGE = "should be in alphabetical order"


class NoncollectionClass:
        @classmethod
        def name(cls):
            return "noncollectionclass"

class MockInvalidCollection_Noncollection(Collection):
    _name = "noncollection"
    _categories = [Adjective, Bird, NoncollectionClass]
    EXPECTED_ERROR_MESSAGE = "contains invalid class: " + str(NoncollectionClass)
