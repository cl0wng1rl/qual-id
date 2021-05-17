import unittest
from qual_id.validators.number_validator import NumberValidator


class TestNumberValidator(unittest.TestCase):
    def test__validate__integer__is_valid_returns_true(self):
        validator = NumberValidator(5)
        validator.validate()
        self.assertTrue(validator.is_valid())

    def test__validate__non_integer__is_valid_returns_false(self):
        validator = NumberValidator("6")
        validator.validate()
        self.assertFalse(validator.is_valid())

    def test__validate__non_integer__error_message_returns_correct_message(self):
        validator = NumberValidator("6")
        validator.validate()
        expected_message = "'number' argument is not an integer"
        self.assertEqual(expected_message, validator.error_message())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
