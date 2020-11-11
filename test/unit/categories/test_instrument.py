import unittest
from qual_id.categories.instrument import Instrument
from test.unit.utils.category_helper import CategoryHelper


class TestInstrument(unittest.TestCase):
    def setUp(self):
        self.instrument = Instrument()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.instrument)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
