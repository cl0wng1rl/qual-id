from qual_id.categories.category import Category


class GroupMetadataValidator:
    """Class to validate the metadata of Groups"""

    @staticmethod
    def validate(group):
        messages = [
            GroupMetadataValidator._get_has_name_error_message(group),
            GroupMetadataValidator._name_lowercase_error_message(group),
            GroupMetadataValidator._get_returns_list_error_message(group),
            GroupMetadataValidator._get_contains_repeats_message(group),
            GroupMetadataValidator._get_contains_non_category_message(group),
            GroupMetadataValidator._get_alphabetical_message(group),
        ]

        error_messages = [message for message in messages if message]
        return "\n".join(error_messages)

    @staticmethod
    def _get_has_name_error_message(group):
        has_name = group.name() != ""
        return "" if has_name else "should have a name"

    @staticmethod
    def _name_lowercase_error_message(group):
        is_lowercase = group.name().lower() == group.name()
        return "" if is_lowercase else "name should be all lowercase"

    @staticmethod
    def _get_returns_list_error_message(group):
        returns_list = GroupMetadataValidator._values_is_a_non_empty_list(group)
        return "" if returns_list else "should return non-empty list"

    @staticmethod
    def _values_is_a_non_empty_list(group):
        is_list = isinstance(group._categories, list)
        is_empty = len(group._categories) == 0
        return is_list and not is_empty

    @staticmethod
    def _get_contains_repeats_message(group):
        repeats = [cat.name() for cat in group._categories]
        uniques = set(repeats)
        [repeats.remove(unique) for unique in uniques]
        repeats = list(map(lambda x: str(x), repeats))
        return GroupMetadataValidator._get_message("contains repeats: ", repeats)

    @staticmethod
    def _get_contains_non_category_message(group):
        invalids = [
            str(value)
            for value in group._categories
            if GroupMetadataValidator._is_not_a_category(value)
        ]
        return GroupMetadataValidator._get_message("contains invalid class: ", invalids)

    @staticmethod
    def _get_alphabetical_message(group):
        message = "should be in alphabetical order"
        values = [cat.name() for cat in group._categories]
        return "" if sorted(values) == values else message

    @staticmethod
    def _get_message(beginning, lst):
        return (beginning + ", ".join(lst)) if len(lst) else ""

    @staticmethod
    def _is_not_a_category(category):
        return category.__base__ != Category
