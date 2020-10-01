import unittest
from qual_id.categories.instrument import Instrument
from test.utils.category_helper import CategoryHelper


class TestInstrument(unittest.TestCase):
  def setUp(self):
    self.instrument = Instrument()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.instrument))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
