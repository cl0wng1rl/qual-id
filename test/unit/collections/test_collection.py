import unittest
from qual_id.categories.fruit import Fruit
from qual_id.categories.fish import Fish
from qual_id.collections.all import All
import random


class TestCollection(unittest.TestCase):
    VALID_KEY = "fruit"
    SECOND_VALID_KEY = "geography"
    THIRD_VALID_KEY = "fish"
    INVALID_KEY = "$$$"
    ALL_COLLECTION_NAME = "all"

    def setUp(self):
        self.collection = All()

    def test__get__valid_key__returns_correct_category(self):
        self.assertIsInstance(self.collection.get(self.VALID_KEY)(), Fruit)
        
    def test__invalid__with_valid_keys__returns_empty_list(self):
        keys_to_validate = [self.VALID_KEY, self.SECOND_VALID_KEY]
        self.assertEqual(self.collection.invalid(keys_to_validate), [])

    def test__invalid__with_an_invalid_key__returns_invalid_key(self):
        keys_to_validate = [self.VALID_KEY, self.INVALID_KEY]
        result = self.collection.invalid(keys_to_validate)
        self.assertEqual(result, [self.INVALID_KEY])
    
    def test__random__mock_random_choice__returns_correct_category(self):
        random.seed(0)
        self.assertIsInstance(self.collection.random()(), Fish)

    def test__name__all_collection__returns_name_all(self):
        self.assertEqual(self.collection.name(), self.ALL_COLLECTION_NAME)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
