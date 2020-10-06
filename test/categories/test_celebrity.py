import unittest
from qual_id.categories.celebrity import Celebrity
from test.utils.category_helper import CategoryHelper


class TestCelebrity(unittest.TestCase):
    def setUp(self):
        self.celebrity = Celebrity()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.celebrity)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
