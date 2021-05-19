import unittest
from qual_id.cli.info.info_factory import InfoFactory
from qual_id.cli.info.flag import Flag
from unittest.mock import patch

class TestInfoFactory(unittest.TestCase):
    COLLECTION_NAME = "collection-name"
    COLLECTION_INFO = ["collection1", "collection2", "collection3"]
    SPECIFIC_COLLECTION_INFO = ["category1", "category2", "category3"]
    CATEGORY_NAME = "category-name"
    CATEGORY_INFO = ["categoryA", "categoryB", "categoryC"]
    SPECIFIC_CATEGORY_INFO = ["value1", "value2", "value3"]
    FORMAT_INFO = ["json", "csv"]

    @patch("qual_id.cli.info.info_factory.CollectionFactory")
    def test__get__collection_and_no_value__correct_info(self, mock_collection_factory):
        self.set_mock_collection_factory(mock_collection_factory)
        info = InfoFactory.get(Flag.COLLECTION)
        self.assertEqual(self.COLLECTION_INFO, info)

    @patch("qual_id.cli.info.info_factory.CollectionFactory")
    def test__get__collection_and_value__correct_info(self, mock_collection_factory):
        self.set_mock_collection_factory(mock_collection_factory)
        info = InfoFactory.get(Flag.COLLECTION, self.COLLECTION_NAME)
        self.assertEqual(self.SPECIFIC_COLLECTION_INFO, info)

    @patch("qual_id.cli.info.info_factory.All")
    def test__get__category_and_no_value__correct_info(self, mock_collection):
        self.set_mock_all_collection(mock_collection)
        info = InfoFactory.get(Flag.CATEGORY)
        self.assertEqual(self.CATEGORY_INFO, info)

    @patch("qual_id.cli.info.info_factory.All")
    def test__get__category_and_value__correct_info(self, mock_collection):
        self.set_mock_collection(mock_collection)
        info = InfoFactory.get(Flag.CATEGORY, self.CATEGORY_NAME)
        self.assertEqual(self.SPECIFIC_CATEGORY_INFO, info)

    def test__get__format_and_no_value__correct_info(self):
        info = InfoFactory.get(Flag.FORMAT)
        self.assertEqual(self.FORMAT_INFO, info)


    def set_mock_collection_factory(self, mock):
        self.set_mock_collection(mock.get.return_value)
        mock.has.return_value = True
        mock.info.return_value = self.COLLECTION_INFO

    def set_mock_collection(self, mock):
        mock.name.return_value = self.COLLECTION_NAME
        mock.info.return_value = self.SPECIFIC_COLLECTION_INFO
        self.set_mock_category(mock.get.return_value)
    
    def set_mock_all_collection(self, mock):
        mock.name.return_value = self.COLLECTION_NAME
        mock.info.return_value = self.CATEGORY_INFO
        self.set_mock_category(mock.get.return_value)
    
    def set_mock_category(self, mock):
        mock.name.return_value = self.CATEGORY_NAME
        mock.info.return_value = self.SPECIFIC_CATEGORY_INFO


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
