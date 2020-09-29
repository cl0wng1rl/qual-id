import unittest
from qual_id.categories.instrument import Instrument
import random


class TestInstrument(unittest.TestCase):
  def setUp(self):
    self.instrument = Instrument()

  def test__get_values__returns_list(self):
    self.assertIsInstance(self.instrument.get_values(), list)
    self.assertGreater(len(self.instrument.get_values()), 0)

  def test__get_values__each_string_is_correct(self):
    for value in self.instrument.get_values():
      self.assertFalse(' ' in value)


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
