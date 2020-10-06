import unittest
from qual_id.categories.state import State
from test.utils.category_helper import CategoryHelper

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.state)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
