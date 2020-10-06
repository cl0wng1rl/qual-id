import unittest
from qual_id.categories.chemicalelement import ChemicalElement
from test.utils.category_helper import CategoryHelper


class TestChemicalElement(unittest.TestCase):
    def setUp(self):
        self.chemicalelement = ChemicalElement()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.chemicalelement)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
