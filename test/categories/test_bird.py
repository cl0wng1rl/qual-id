import unittest
from qual_id.categories.bird import Bird
from test.utils.category_helper import CategoryHelper


class TestBird(unittest.TestCase):
    def setUp(self):
        self.bird = Bird()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.bird)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
