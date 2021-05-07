import unittest
from qual_id.category import Category
from qual_id.collections.all import All


class TestCollection(unittest.TestCase):
    VALID_KEY = "fruit"
    SECOND_VALID_KEY = "geography"
    THIRD_VALID_KEY = "bird"
    INVALID_KEY = "$$$"

    def setUp(self):
        self.collection = All()

    def test__get__valid_key__returns_category(self):
        self.assertIsInstance(self.collection.get(self.VALID_KEY)(), Category)
        
    def test__invalid__with_valid_keys__returns_empty_list(self):
        keys_to_validate = [self.VALID_KEY, self.SECOND_VALID_KEY]
        self.assertEqual(self.collection.invalid(keys_to_validate), [])

    def test__invalid__with_an_invalid_key__returns_invalid_key(self):
        keys_to_validate = [self.VALID_KEY, self.INVALID_KEY]
        result = self.collection.invalid(keys_to_validate)
        self.assertEqual(result, [self.INVALID_KEY])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
