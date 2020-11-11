import unittest
from qual_id.category import Category
from qual_id.category_map import CategoryMap


class TestCategoryMap(unittest.TestCase):
    VALID_KEY = "fruit"
    SECOND_VALID_KEY = "geography"
    THIRD_VALID_KEY = "bird"
    INVALID_KEY = "$$$"

    def setUp(self):
        self.category_map = CategoryMap()

    def test__get__valid_key__returns_category(self):
        self.assertIsInstance(self.category_map.get(self.VALID_KEY), Category)

    def test__has__valid_key__returns_true(self):
        self.assertTrue(self.category_map.has(self.VALID_KEY))
        self.assertTrue(self.category_map.has(self.SECOND_VALID_KEY))
        self.assertTrue(self.category_map.has(self.THIRD_VALID_KEY))

    def test__has__invalid_key__returns_false(self):
        self.assertFalse(self.category_map.has(self.INVALID_KEY))

    def test__constructed_with_list__only_has_give_keys(self):
        keys = [self.VALID_KEY, self.SECOND_VALID_KEY]
        self.category_map = CategoryMap(keys)
        self.assertTrue(self.category_map.has(self.VALID_KEY))
        self.assertTrue(self.category_map.has(self.SECOND_VALID_KEY))
        self.assertFalse(self.category_map.has(self.THIRD_VALID_KEY))

    def test__invalid__with_valid_keys__returns_empty_list(self):
        keys_to_validate = [self.VALID_KEY, self.SECOND_VALID_KEY]
        self.assertEqual(self.category_map.invalid(keys_to_validate), [])

    def test__invalid__with_an_invalid_key__returns_invalid_key(self):
        keys_to_validate = [self.VALID_KEY, self.INVALID_KEY]
        result = self.category_map.invalid(keys_to_validate)
        self.assertEqual(result, [self.INVALID_KEY])

    def test__categories__default__returns_alphabetical_list(self):
        error_message = "categories should be listed in alphabetical order"
        categories = CategoryMap().categories()
        self.assertEqual(categories, sorted(categories), error_message)

    def test__categories__returns_keys(self):
        keys = [self.VALID_KEY, self.SECOND_VALID_KEY]
        self.category_map = CategoryMap(keys)
        categories = self.category_map.categories()
        self.assertEqual(keys, categories)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
