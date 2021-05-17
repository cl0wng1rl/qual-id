import unittest
from qual_id.collections.collection import Collection
from qual_id.collections import CollectionFactory


class TestCollectionFactory(unittest.TestCase):
    def test__get__all__correct_category(self):
        self.assert_is_collection("all")

    def test__get__minimal__correct_category(self):
        self.assert_is_collection("minimal")

    def test__has__invalid_string__false(self):
        self.assertFalse(CollectionFactory.has("$$$"))

    def test__has__minimal__true(self):
        self.assertTrue(CollectionFactory.has("minimal"))

    def test__info__non_empty_list_of_collections(self):
        self.assertTrue(CollectionFactory.info())
        [self.assert_is_collection(name) for name in CollectionFactory.info()]

    def assert_is_collection(self, name):
        self.assertEqual(CollectionFactory.get(name).__base__, Collection)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
