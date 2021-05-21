import unittest
from qual_id.cli.info.info_flag import InfoFlag


class TestInfoFlag(unittest.TestCase):
    """Unit Tests for InfoFlag"""

    LONG = "flag"
    SHORT = "f"
    LONG_FLAG = "--flag"
    SHORT_FLAG = "-f"
    WRONG_FLAG = "--wrongflag"
    IS_SINGULAR = True

    def setUp(self):
        self.flag = InfoFlag(self.LONG, self.SHORT, self.IS_SINGULAR)

    def test__name__correct_name(self):
        """InfoFlag -> name - correct name"""
        self.assertEqual(self.LONG, self.flag.name())

    def test__equals__long_flag__true(self):
        """InfoFlag -> equals - long flag"""
        self.assertTrue(self.flag.equals(self.LONG_FLAG))

    def test__equals__short_flag__true(self):
        """InfoFlag -> equals - short flag"""
        self.assertTrue(self.flag.equals(self.SHORT_FLAG))

    def test__equals__wrong_flag__false(self):
        """InfoFlag -> equals - wrong flag"""
        self.assertFalse(self.flag.equals(self.WRONG_FLAG))

    def test__is_singular__correct_boolean_value(self):
        """InfoFlag -> is_singular"""
        self.assertEqual(self.IS_SINGULAR, self.flag.is_singular())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
