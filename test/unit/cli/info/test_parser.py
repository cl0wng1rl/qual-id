import unittest
from qual_id.cli.info.parser import Parser
from qual_id.cli.info.validator import Validator
from qual_id.cli.info.flag import Flag
from unittest.mock import Mock, patch


class TestParser(unittest.TestCase):
    COMMAND_NAME = "qid"
    INFO_FLAG = "--info"
    PARAMETER = Flag.CATEGORY
    PARAMETER_NAME = "category"
    VALUE = "category-value"
    INFO = ["value1", "value2", "value3"]

    @patch("qual_id.cli.info.parser.InfoFactory")
    @patch("qual_id.cli.info.parser.InfoConfig")
    def test__parse__category__correct_config(
        self, mock_info_config, mock_info_factory
    ):
        mock_config = Mock()
        mock_info_config.return_value = mock_config
        self.set_mock_info_factory(mock_info_factory)

        config = Parser().parse(self.get_valid_args__category())
        mock_info_config.assert_called_with(self.PARAMETER, None, self.INFO)
        self.assertEqual(mock_config, config)

    @patch("qual_id.cli.info.parser.InfoFactory")
    @patch("qual_id.cli.info.parser.InfoConfig")
    def test__parse__category_and_value__correct_config(
        self, mock_info_config, mock_info_factory
    ):
        mock_config = Mock()
        mock_info_config.return_value = mock_config
        self.set_mock_info_factory(mock_info_factory)

        config = Parser().parse(self.get_valid_args__category_and_value())
        mock_info_config.assert_called_with(self.PARAMETER, self.VALUE, self.INFO)
        self.assertEqual(mock_config, config)

    def set_mock_info_factory(self, mock):
        mock.get.return_value = self.INFO

    def get_valid_args__category(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.PARAMETER_NAME]

    def get_valid_args__category_and_value(self):
        return [self.COMMAND_NAME, self.INFO_FLAG, self.PARAMETER_NAME, self.VALUE]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
