import unittest
import random
from qual_id.collections.collection import Collection
from qual_id.collections.all import All
from qual_id.categories import Adjective, Bird, Cake, Fish


class TestCollection(unittest.TestCase):
    COLLECTION_NAME = "collection"
    COLLECTION_VALUES = [Adjective, Bird, Cake]
    VALID_KEYS = [Adjective.name(), Bird.name(), Cake.name()]
    INVALID_KEY = Fish.name()

    def setUp(self):
        self.collection = MockCollection()

    def test__get__valid_key__correct_category(self):
        self.assertIsInstance(self.collection.get(self.VALID_KEYS[0])(), Adjective)
        
    def test__invalid__valid_keys__empty_list(self):
        self.assertEqual(self.collection.invalid(self.VALID_KEYS), [])

    def test__invalid__an_invalid_key__invalid_key(self):
        keys_to_validate = [self.VALID_KEYS[0], self.INVALID_KEY]
        result = self.collection.invalid(keys_to_validate)
        self.assertEqual(result, [self.INVALID_KEY])
    
    def test__random__mock_random_choice__correct_category(self):
        random.seed(0)
        self.assertIsInstance(self.collection.random()(), Bird)

    def test__name__correct_name(self):
        self.assertEqual(self.collection.name(), self.COLLECTION_NAME)

    def test__info__correct_values(self):
        self.assertEqual(self.collection.info(), self.VALID_KEYS)

class MockCollection(Collection):
    _name = TestCollection.COLLECTION_NAME
    _categories = TestCollection.COLLECTION_VALUES

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
