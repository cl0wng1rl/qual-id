import unittest
from qual_id.categories.operatingsystem import OperatingSystem
from test.utils.category_helper import CategoryHelper


class TestOperatingSystem(unittest.TestCase):
    def setUp(self):
        self.operatingsystem = OperatingSystem()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.operatingsystem)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
