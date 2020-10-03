import unittest
from qual_id.categories.company import Company
from test.utils.category_helper import CategoryHelper


class TestElectronic(unittest.TestCase):
    def setUp(self):
        self.company = Company()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.company)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()