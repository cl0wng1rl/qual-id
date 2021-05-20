import unittest
import random
from qual_id.groups.group import Group
from qual_id.groups.all import All
from qual_id.categories import Adjective, Bird, Cake, Fish


class TestGroup(unittest.TestCase):
    GROUP_NAME = "group"
    GROUP_VALUES = [Adjective, Bird, Cake]
    VALID_KEYS = [Adjective.name(), Bird.name(), Cake.name()]
    INVALID_KEY = Fish.name()

    def setUp(self):
        self.group = MockGroup()

    def test__get__valid_key__correct_category(self):
        self.assertIsInstance(self.group.get(self.VALID_KEYS[0])(), Adjective)
        
    def test__invalid__valid_keys__empty_list(self):
        self.assertEqual(self.group.invalid(self.VALID_KEYS), [])

    def test__invalid__an_invalid_key__invalid_key(self):
        keys_to_validate = [self.VALID_KEYS[0], self.INVALID_KEY]
        result = self.group.invalid(keys_to_validate)
        self.assertEqual(result, [self.INVALID_KEY])
    
    def test__random__mock_random_choice__correct_category(self):
        random.seed(0)
        self.assertIsInstance(self.group.random()(), Bird)

    def test__name__correct_name(self):
        self.assertEqual(self.group.name(), self.GROUP_NAME)

    def test__info__correct_values(self):
        self.assertEqual(self.group.info(), self.VALID_KEYS)

class MockGroup(Group):
    _name = TestGroup.GROUP_NAME
    _categories = TestGroup.GROUP_VALUES

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
