import unittest
from qual_id.cli.info.info_factory import InfoFactory
from qual_id.cli.info.flag import Flag
from unittest.mock import patch

class TestInfoFactory(unittest.TestCase):
    GROUP_NAME = "group-name"
    GROUP_INFO = ["group1", "group2", "group3"]
    SPECIFIC_GROUP_INFO = ["category1", "category2", "category3"]
    CATEGORY_NAME = "category-name"
    CATEGORY_INFO = ["categoryA", "categoryB", "categoryC"]
    SPECIFIC_CATEGORY_INFO = ["value1", "value2", "value3"]
    FORMAT_INFO = ["json", "csv"]

    @patch("qual_id.cli.info.info_factory.GroupFactory")
    def test__get__group_and_no_value__correct_info(self, mock_group_factory):
        self.set_mock_group_factory(mock_group_factory)
        info = InfoFactory.get(Flag.GROUP)
        self.assertEqual(self.GROUP_INFO, info)

    @patch("qual_id.cli.info.info_factory.GroupFactory")
    def test__get__group_and_value__correct_info(self, mock_group_factory):
        self.set_mock_group_factory(mock_group_factory)
        info = InfoFactory.get(Flag.GROUP, self.GROUP_NAME)
        self.assertEqual(self.SPECIFIC_GROUP_INFO, info)

    @patch("qual_id.cli.info.info_factory.All")
    def test__get__category_and_no_value__correct_info(self, mock_group):
        self.set_mock_all_group(mock_group)
        info = InfoFactory.get(Flag.CATEGORY)
        self.assertEqual(self.CATEGORY_INFO, info)

    @patch("qual_id.cli.info.info_factory.All")
    def test__get__category_and_value__correct_info(self, mock_group):
        self.set_mock_group(mock_group)
        info = InfoFactory.get(Flag.CATEGORY, self.CATEGORY_NAME)
        self.assertEqual(self.SPECIFIC_CATEGORY_INFO, info)

    def test__get__format_and_no_value__correct_info(self):
        info = InfoFactory.get(Flag.FORMAT)
        self.assertEqual(self.FORMAT_INFO, info)

    @patch("qual_id.cli.info.info_factory.GroupFactory")
    def test__has__group_and_value__correct_boolean(self, mock_group_factory):
        self.set_mock_group_factory(mock_group_factory)
        has = InfoFactory.has(Flag.GROUP, self.GROUP_NAME)
        self.assertEqual(True, has)

    @patch("qual_id.cli.info.info_factory.All")
    def test__has__category_and_value__correct_boolean(self, mock_group):
        self.set_mock_group(mock_group)
        has = InfoFactory.has(Flag.CATEGORY, self.CATEGORY_NAME)
        self.assertEqual(True, has)


    def set_mock_group_factory(self, mock):
        self.set_mock_group(mock.get.return_value)
        mock.has.return_value = True
        mock.info.return_value = self.GROUP_INFO

    def set_mock_group(self, mock):
        mock.name.return_value = self.GROUP_NAME
        mock.info.return_value = self.SPECIFIC_GROUP_INFO
        self.set_mock_category(mock.get.return_value)
    
    def set_mock_all_group(self, mock):
        mock.name.return_value = self.GROUP_NAME
        mock.info.return_value = self.CATEGORY_INFO
        self.set_mock_category(mock.get.return_value)
    
    def set_mock_category(self, mock):
        mock.name.return_value = self.CATEGORY_NAME
        mock.info.return_value = self.SPECIFIC_CATEGORY_INFO


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
