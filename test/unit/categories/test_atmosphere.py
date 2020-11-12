import unittest
from qual_id.categories.atmosphere import Atmosphere
from test.unit.utils.category_helper import CategoryHelper


class TestAtmosphere(unittest.TestCase):
    def setUp(self):
        self.atmosphere = Atmosphere()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.atmosphere)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
