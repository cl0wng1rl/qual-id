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

    def test__constructed_with_list__only_has_give_keys(self):
        keys = [self.VALID_KEY, self.SECOND_VALID_KEY]
        self.category_map = CategoryMap(keys)
        keys_to_test = [self.VALID_KEY, self.SECOND_VALID_KEY, self.THIRD_VALID_KEY]
        expected = [self.THIRD_VALID_KEY]
        self.assertEqual(expected, self.category_map.invalid(keys_to_test))

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
