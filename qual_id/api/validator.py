from qual_id.groups import GroupFactory


class Validator:
    @staticmethod
    def validate(args):
        return Validator._validate(args["group"], args["categories"], args["number"], args["format"])

    @staticmethod
    def _validate(group_name, category_names, number, format_string):
        error_message = (
            Validator._validate_group(group_name)
            or Validator._validate_categories(group_name, category_names)
            or Validator._validate_number(number)
            or Validator._validate_format(format_string)
        )
        return error_message or None

    @staticmethod
    def _validate_group(group_name):
        error_message = "Group '{0}' does not exist.".format(group_name)
        return (not GroupFactory.has(group_name)) and error_message

    @staticmethod
    def _validate_categories(group_name, category_names):
        invalid = GroupFactory.get(group_name).invalid(category_names)
        error_message = "Categories do not exist: '{0}'.".format(", ".join(invalid))
        return len(invalid) > 0 and error_message

    @staticmethod
    def _validate_number(number):
        error_message = "Number argument is not an integer."
        return not number.isdigit() and error_message

    @staticmethod
    def _validate_format(format_string):
        error_message = "Format must be 'json' or 'csv'."
        return (not format_string in ["json", "csv"]) and error_message
