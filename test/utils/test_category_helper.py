import unittest
from qual_id.category import Category
from test.utils.category_helper import CategoryHelper


class TestCategoryHelper(unittest.TestCase):
    def setUp(self):
        self.category = None

    def test__get_values_is_valid__with_valid_category__returns_true(self):
        self.category = MockCategoryWithValidGetValuesMethod()
        self.assertTrue(CategoryHelper.get_values_is_valid(self.category))

    def test__get_values_is_valid__with_invalid_category_due_to_spaces__returns_false(
        self,
    ):
        self.category = MockCategoryWithInvalidGetValuesMethod_Spaces()
        self.assertFalse(CategoryHelper.get_values_is_valid(self.category))

    def test__get_values_is_valid__with_invalid_category_due_to_dashes__returns_false(
        self,
    ):
        self.category = MockCategoryWithInvalidGetValuesMethod_Dashes()
        self.assertFalse(CategoryHelper.get_values_is_valid(self.category))

    def test__get_values_is_valid__with_invalid_category_due_to_empty_list__returns_false(
        self,
    ):
        self.category = MockCategoryWithInvalidGetValuesMethod_Empty()
        self.assertFalse(CategoryHelper.get_values_is_valid(self.category))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()


class MockCategoryWithValidGetValuesMethod(Category):
    def get_values(self):
        return [
            "valueA",
            "valueB",
            "valueC",
        ]


class MockCategoryWithInvalidGetValuesMethod_Spaces(Category):
    def get_values(self):
        return [
            "value A",
            "value B",
            "value C",
        ]


class MockCategoryWithInvalidGetValuesMethod_Dashes(Category):
    def get_values(self):
        return [
            "value-A",
            "value-B",
            "value-C",
        ]


class MockCategoryWithInvalidGetValuesMethod_Empty(Category):
    def get_values(self):
        return []
