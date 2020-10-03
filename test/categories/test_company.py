import unittest
from qual_id.categories.company import Company
from test.utils.category_helper import CategoryHelper


class TestCompany(unittest.TestCase):
  def setUp(self):
    self.company = Company()

  def test__get_values__is_valid(self):
        self.assertTrue(CategoryHelper.get_values_is_valid(self.company))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
