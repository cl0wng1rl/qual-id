import unittest
from qual_id.categories.tool import Tool
from test.utils.category_helper import CategoryHelper


class TestTool(unittest.TestCase):
    def setUp(self):
        self.tool = Tool()
    def test__get_values__is_valid(self):
        self.assertTrue(CategoryHelper.get_values_is_valid(self.tool))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()