import unittest
from qual_id.pattern import Pattern
from unittest.mock import MagicMock


class TestPattern(unittest.TestCase):
  def setUp(self):
    self.pattern = None

  def test__get_category_options__returns_non_empty_list(self):
    self.pattern = Pattern('test_pattern')
    self.assertGreater(len(self.pattern.get_category_options()), 0)

  def test__has_acceptable_categories_length__valid_number_of_categories_returns_true(self):
    self.pattern = Pattern('test_pattern')
    categories = self.pattern.get_category_options()

    self.pattern = Pattern('-'.join([categories[0], categories[1]]))
    self.assertTrue(self.pattern.has_acceptable_categories_length())

  def test__get_nonexistent_categories__nonempty_invalid_category_list__returns_false(self):
    self.pattern = Pattern('invalid_pattern')
    self.assertTrue(len(self.pattern.get_nonexistent_categories()) > 0)

  def test__has_acceptable_categories_length__pattern_with_more_than_5_categories__returns_false(self):
    self.pattern = Pattern('test_pattern')
    categories = self.pattern.get_category_options()

    self.pattern = Pattern('-'.join([categories[0]] * 6))
    self.assertFalse(self.pattern.has_acceptable_categories_length())

  def test__has_acceptable_categories_length__empty_pattern__returns_false(self):
    self.pattern = Pattern('')
    self.assertFalse(self.pattern.has_acceptable_categories_length())

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
