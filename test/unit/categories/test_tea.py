import unittest
from qual_id.categories.tea import Tea
from test.unit.utils.category_helper import CategoryHelper


class TestTea(unittest.TestCase):
    def setUp(self):
        self.tea = Tea()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.tea)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
