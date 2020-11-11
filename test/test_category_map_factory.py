import unittest
from qual_id.category_map import CategoryMap
from qual_id.category_map_factory import CategoryMapFactory


class TestCategoryMapFactory(unittest.TestCase):
    def test__get__empty_string__returns_category(self):
        self.assertIsInstance(CategoryMapFactory.get(""), CategoryMap)

    def test__get__minimal__returns_category(self):
        self.assertIsInstance(CategoryMapFactory.get("minimal"), CategoryMap)

    def test__get__neutral__returns_category(self):
        self.assertIsInstance(CategoryMapFactory.get("neutral"), CategoryMap)

    def test__has__invalid_string__returns_false(self):
        self.assertFalse(CategoryMapFactory.has("$$$"))

    def test__has__minimal__returns_false(self):
        self.assertTrue(CategoryMapFactory.has("minimal"))

    def test__has__neutral__returns_false(self):
        self.assertTrue(CategoryMapFactory.has("neutral"))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
