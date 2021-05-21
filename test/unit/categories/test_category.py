import unittest
from qual_id.categories.category import Category
import random


class TestCategory(unittest.TestCase):
    """Unit Tests for Category"""

    CATEGORY_NAME = "category"
    CATEGORY_VALUES = ["valuea", "valueb", "valuec"]

    def test__name__correct_name(self):
        """Category -> name"""
        self.assertEqual(MockCategory.name(), TestCategory.CATEGORY_NAME)

    def test__random__mock_random_choice__correct_value(self):
        """Category -> random"""
        random.seed(0)
        fixed_choice = TestCategory.CATEGORY_VALUES[1]
        self.assertEqual(MockCategory.random(), fixed_choice)

    def test__info__correct_values(self):
        """Category -> info"""
        self.assertListEqual(MockCategory.info(), TestCategory.CATEGORY_VALUES)


class MockCategory(Category):
    _name = TestCategory.CATEGORY_NAME
    _values = TestCategory.CATEGORY_VALUES


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
