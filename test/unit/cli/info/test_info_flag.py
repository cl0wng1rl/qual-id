import unittest
from qual_id.cli.info.info_flag import InfoFlag


class TestInfoFlag(unittest.TestCase):
    NAME = "Flag Name"
    IS_SINGULAR = True

    def setUp(self):
        self.flag = InfoFlag(self.NAME, self.IS_SINGULAR)

    def test__name__correct_name(self):
        self.assertEqual(self.NAME, self.flag.name())

    def test__is_singular__correct_boolean_value(self):
        self.assertEqual(self.IS_SINGULAR, self.flag.is_singular())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
