import unittest
from qual_id.collections.collection import Collection
from qual_id.collections import CollectionFactory


class TestCollectionFactory(unittest.TestCase):
    def test__get__all__returns_category(self):
        self.assertEqual(CollectionFactory.get("all").__base__, Collection)

    def test__get__minimal__returns_category(self):
        self.assertEqual(CollectionFactory.get("minimal").__base__, Collection)

    def test__get__neutral__returns_category(self):
        self.assertEqual(CollectionFactory.get("neutral").__base__, Collection)

    def test__has__invalid_string__returns_false(self):
        self.assertFalse(CollectionFactory.has("$$$"))

    def test__has__minimal__returns_false(self):
        self.assertTrue(CollectionFactory.has("minimal"))

    def test__has__neutral__returns_false(self):
        self.assertTrue(CollectionFactory.has("neutral"))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
