import unittest
from qual_id.categories.language import Language
from test.unit.utils.category_helper import CategoryHelper


class TestLanguage(unittest.TestCase):
    def setUp(self):
        self.language = Language()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.language)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
