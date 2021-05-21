import unittest
import random
from qual_id.groups.group import Group
from qual_id.groups.all import All
from qual_id.categories import Adjective, Bird, Cake, Fish


class TestGroup(unittest.TestCase):
    GROUP_NAME = "group"
    GROUP_VALUES = [Adjective, Bird, Cake]
    RANDOM_NAME = "random"
    VALID_NAMES = [Adjective.name(), Bird.name(), Cake.name()]
    INVALID_NAME = Fish.name()

    def setUp(self):
        self.group = MockGroup()

    def test__get__valid_name__correct_category(self):
        self.assertIsInstance(self.group.get(self.VALID_NAMES[0])(), Adjective)

    def test__invalid__valid_names__empty_list(self):
        self.assertEqual(self.group.invalid(self.VALID_NAMES), [])

    def test__invalid__an_invalid_name__invalid_name(self):
        names_to_validate = [self.VALID_NAMES[0], self.INVALID_NAME]
        result = self.group.invalid(names_to_validate)
        self.assertEqual(result, [self.INVALID_NAME])

    def test__get__random_name__correct_category(self):
        random.seed(0)
        self.assertIsInstance(self.group.get(self.RANDOM_NAME)(), Bird)

    def test__name__correct_name(self):
        self.assertEqual(self.group.name(), self.GROUP_NAME)

    def test__info__correct_values(self):
        self.assertEqual(self.group.info(), self.VALID_NAMES)


class MockGroup(Group):
    _name = TestGroup.GROUP_NAME
    _categories = TestGroup.GROUP_VALUES


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
