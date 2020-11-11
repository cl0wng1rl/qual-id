import unittest
from qual_id.category_map import CategoryMap
from qual_id.category_map_factory import CategoryMapFactory


class TestCategoryMapFactory(unittest.TestCase):
    def test__all__returns_category_map(self):
        self.assertIsInstance(CategoryMapFactory.get(""), CategoryMap)

    def test__minimal__returns_category(self):
        self.assertIsInstance(CategoryMapFactory.get("minimal"), CategoryMap)

    def test__neutral__returns_category(self):
        self.assertIsInstance(CategoryMapFactory.get("neutral"), CategoryMap)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
