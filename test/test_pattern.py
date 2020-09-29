import unittest
from qual_id.pattern import Pattern
from unittest.mock import MagicMock


class TestPattern(unittest.TestCase):
  def setUp(self):
    self.pattern = None

  def test__get_category_options__returns_non_empty_list(self):
    self.pattern = Pattern('test_pattern')
    self.assertGreater(len(self.pattern.get_category_options()), 0)

  def test__is_valid__valid_pattern_from_category_options_returns_true(self):
    self.pattern = Pattern('test_pattern')
    categories = self.pattern.get_category_options()

    self.pattern = Pattern('-'.join([categories[0], categories[1]]))
    self.assertTrue(self.pattern.is_valid())

  def test__is_valid__invalid_pattern__returns_false(self):
    self.pattern = Pattern('invalid_pattern')
    self.assertFalse(self.pattern.is_valid())

  def test__is_valid__pattern_with_more_than_5_categories__returns_false(self):
    self.pattern = Pattern('test_pattern')
    categories = self.pattern.get_category_options()

    self.pattern = Pattern('-'.join([categories[0]] * 6))
    self.assertFalse(self.pattern.is_valid())

  def test__get_categories__pattern_from_categories__returns_array_of_correct_length(self):
    self.pattern = Pattern('test_pattern')
    categories = self.pattern.get_category_options()

    self.pattern = Pattern('-'.join([categories[0], categories[1]]))
    categories = self.pattern.get_categories()
    self.assertEqual(len(categories), 2)
    [self.assertNotEqual(category, None) for category in categories]

  def test__get_categories__pattern_with_randoms__returns_array_of_correct_length(self):
    self.pattern = Pattern('-'.join(['random'] * 2))
    categories = self.pattern.get_categories()
    self.assertEqual(len(categories), 2)
    [self.assertNotEqual(category, None) for category in categories]


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
