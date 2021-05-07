import unittest
from qual_id.collection import Collection
from qual_id.collection_factory import CollectionFactory


class TestCollectionFactory(unittest.TestCase):
    def test__get__all__returns_category(self):
        self.assertIsInstance(CollectionFactory.get("all"), Collection)

    def test__get__minimal__returns_category(self):
        self.assertIsInstance(CollectionFactory.get("minimal"), Collection)

    def test__get__neutral__returns_category(self):
        self.assertIsInstance(CollectionFactory.get("neutral"), Collection)

    def test__has__invalid_string__returns_false(self):
        self.assertFalse(CollectionFactory.has("$$$"))

    def test__has__minimal__returns_false(self):
        self.assertTrue(CollectionFactory.has("minimal"))

    def test__has__neutral__returns_false(self):
        self.assertTrue(CollectionFactory.has("neutral"))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
