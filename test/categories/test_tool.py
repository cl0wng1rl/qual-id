import unittest
from qual_id.categories.tool import Tool
from test.utils.category_helper import CategoryHelper


class TestTool(unittest.TestCase):
    def setUp(self):
        self.tool = Tool()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.tool)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
