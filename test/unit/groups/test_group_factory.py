import unittest
from qual_id.groups.group import Group
from qual_id.groups import GroupFactory


class TestGroupFactory(unittest.TestCase):
    def test__get__all__correct_category(self):
        self.assert_is_group("all")

    def test__get__minimal__correct_category(self):
        self.assert_is_group("minimal")

    def test__has__invalid_string__false(self):
        self.assertFalse(GroupFactory.has("$$$"))

    def test__has__minimal__true(self):
        self.assertTrue(GroupFactory.has("minimal"))

    def test__info__non_empty_list_of_groups(self):
        self.assertTrue(GroupFactory.info())
        [self.assert_is_group(name) for name in GroupFactory.info()]

    def assert_is_group(self, name):
        self.assertEqual(GroupFactory.get(name).__base__, Group)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
