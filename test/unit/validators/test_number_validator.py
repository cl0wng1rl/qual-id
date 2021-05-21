import unittest
from qual_id.validators.number_validator import NumberValidator


class TestNumberValidator(unittest.TestCase):
    """Unit Tests for NumberValidator"""

    def test__validate__integer__true(self):
        """NumberValidator -> validate - integer"""
        validator = NumberValidator(5)
        validator.validate()
        self.assertTrue(validator.is_valid())

    def test__validate__non_integer__false(self):
        """NumberValidator -> validate - non-integer"""
        validator = NumberValidator("6")
        validator.validate()
        self.assertFalse(validator.is_valid())

    def test__error_message__non_integer__correct_message(self):
        """NumberValidator -> error_message - non-integer"""
        validator = NumberValidator("6")
        validator.validate()
        expected_message = "'number' argument is not an integer"
        self.assertEqual(expected_message, validator.error_message())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
