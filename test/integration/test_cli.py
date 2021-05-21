import unittest
from qual_id.cli import CLI
import random


class TestCLI_Integration(unittest.TestCase):
    def setUp(self):
        random.seed(1)

    def test__run__long_flags_and_csv_format__expected_response(self):
        self.assert_scenario(LongFlagsAndCSVFormatScenario())

    def test__run__short_flags_and_json_format__expected_response(self):
        self.assert_scenario(ShortFlagsAndJSONFormatScenario())

    def test__run__random_pattern__expected_response(self):
        self.assert_scenario(RandomPatternScenario())

    def test__run__info_group_without_value__expected_response(self):
        self.assert_scenario(GroupWithoutValueScenario())

    def test__run__info_category_with_value__expected_response(self):
        self.assert_scenario(CategoryWithValueScenario())

    def assert_scenario(self, scenario):
        self.assertEqual(scenario.expected(), CLI.run(scenario.arguments()))


class Scenario:
    COMMAND_NAME = "qid"
    INFO_FLAG = "--info"
    INFO_FLAG_SHORT = "-i"
    PATTERN_FLAG = "--pattern"
    PATTERN_FLAG_SHORT = "-p"
    PATTERN = "fruit-geography"
    RANDOM_PATTERN = "random-random"
    GROUP_FLAG = "--group"
    GROUP_FLAG_SHORT = "-g"
    GROUP = "all"
    FORMAT_FLAG = "--format"
    FORMAT_FLAG_SHORT = "-f"
    FORMAT_CSV = "csv"
    FORMAT_JSON = "json"
    NUMBER_FLAG = "--number"
    NUMBER_FLAG_SHORT = "-n"
    CATEGORY_FLAG = "--category"
    CATEGORY_FLAG_SHORT = "-c"
    CATEGORY = "bread"
    NUMBER = "3"

    @classmethod
    def arguments(cls):
        return cls._arguments

    @classmethod
    def expected(cls):
        return cls._expected


class LongFlagsAndCSVFormatScenario(Scenario):
    _arguments = [
        Scenario.COMMAND_NAME,
        Scenario.PATTERN_FLAG,
        Scenario.PATTERN,
        Scenario.GROUP_FLAG,
        Scenario.GROUP,
        Scenario.FORMAT_FLAG,
        Scenario.FORMAT_CSV,
        Scenario.NUMBER_FLAG,
        Scenario.NUMBER,
    ]
    _expected = "coconut-sky,blackberry-hill,clementine-plateau"


class ShortFlagsAndJSONFormatScenario(Scenario):
    _arguments = [
        Scenario.COMMAND_NAME,
        Scenario.PATTERN_FLAG_SHORT,
        Scenario.PATTERN,
        Scenario.GROUP_FLAG_SHORT,
        Scenario.GROUP,
        Scenario.FORMAT_FLAG_SHORT,
        Scenario.FORMAT_JSON,
        Scenario.NUMBER_FLAG_SHORT,
        Scenario.NUMBER,
    ]
    _expected = {"data": ["coconut-sky", "blackberry-hill", "clementine-plateau"]}


class RandomPatternScenario(Scenario):
    _arguments = [
        Scenario.COMMAND_NAME,
        Scenario.PATTERN_FLAG_SHORT,
        Scenario.RANDOM_PATTERN,
        Scenario.GROUP_FLAG_SHORT,
        Scenario.GROUP,
        Scenario.FORMAT_FLAG_SHORT,
        Scenario.FORMAT_CSV,
        Scenario.NUMBER_FLAG_SHORT,
        Scenario.NUMBER,
    ]
    _expected = "turnover-jupiter,donut-jupiter,gingerbread-venus"


class GroupWithoutValueScenario(Scenario):
    _arguments = [
        Scenario.COMMAND_NAME,
        Scenario.INFO_FLAG,
        Scenario.GROUP_FLAG,
    ]
    _expected = "Options for 'group' parameter: \nall, minimal, neutral"


class CategoryWithValueScenario(Scenario):
    _arguments = [
        Scenario.COMMAND_NAME,
        Scenario.INFO_FLAG,
        Scenario.CATEGORY_FLAG_SHORT,
        Scenario.CATEGORY,
    ]
    _expected = ("Values for the category, 'bread': \n"
    "bagel, baguette, brioche, bun, chapati, ciabatta, cornbread, croissant, "
    "focaccia, granary, matzo, muffin, naan, paratha, pitta, poppadom, "
    "pumpernickel, roll, roti, rye, sourdough, tortilla, wholemeal")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
