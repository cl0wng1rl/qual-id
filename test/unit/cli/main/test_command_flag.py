import unittest
from qual_id.cli.main.command_flag import CommandFlag


class TestCommandFlag(unittest.TestCase):
    LONG = "long"
    SHORT = "short"

    def setUp(self):
        self.flag = CommandFlag(self.LONG, self.SHORT)

    def test__name__returns_name(self):
        self.assertEqual(self.LONG, self.flag.name())

    def test__equals__correct_long_flag__true(self):
        self.assertTrue(self.flag.equals("--{0}".format(self.LONG)))

    def test__equals__correct_short_flag__true(self):
        self.assertTrue(self.flag.equals("-{0}".format(self.SHORT)))

    def test__equals__incorrect_long_flag__false(self):
        self.assertFalse(self.flag.equals("-{0}".format(self.LONG)))

    def test__equals__incorrect_short_flag__false(self):
        self.assertFalse(self.flag.equals("--{0}".format(self.SHORT)))

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
