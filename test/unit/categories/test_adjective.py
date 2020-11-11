import unittest
from qual_id.categories.adjective import Adjective
from test.unit.utils.category_helper import CategoryHelper


class TestAdjective(unittest.TestCase):
    def setUp(self):
        self.adjective = Adjective()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.adjective)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
