import unittest
from qual_id.cli.info.flag import Flag
from qual_id.cli.info.info_config import InfoConfig


class TestInfoConfig(unittest.TestCase):
    """Unit Tests for InfoConfig"""

    TYPE = Flag.CATEGORY
    TYPE_NAME = Flag.CATEGORY.value.name()
    VALUE = "value"
    INFO = ["value1", "value2", "value3"]
    INFO_STRING = ", ".join(INFO)

    def test__message__value__correct_message(self):
        """InfoConfig -> message - value"""
        config = InfoConfig(self.TYPE, self.VALUE, self.INFO)
        excepted_message = "Values for the {0}, '{1}': \n{2}".format(
            self.TYPE_NAME, self.VALUE, self.INFO_STRING
        )
        self.assertEqual(excepted_message, config.message())

    def test__message__no_value__correct_message(self):
        """InfoConfig -> message - no value"""
        config = InfoConfig(self.TYPE, None, self.INFO)
        excepted_message = "Options for '{0}' parameter: \n{1}".format(
            self.TYPE_NAME, self.INFO_STRING
        )
        self.assertEqual(excepted_message, config.message())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
