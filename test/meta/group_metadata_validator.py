from qual_id.categories.category import Category

class GroupMetadataValidator:
    """Class to validate the metadata of Groups"""

    __disallowed_characters = [" ", "-", "_", "&"]

    @staticmethod
    def validate(group):
        messages = [
            GroupMetadataValidator.__get_has_name_error_message(group),
            GroupMetadataValidator.__name_lowercase_error_message(group),
            GroupMetadataValidator.__get_returns_list_error_message(group),
            GroupMetadataValidator.__get_contains_repeats_message(group),
            GroupMetadataValidator.__get_contains_non_category_message(group),
            GroupMetadataValidator.__get_alphabetical_message(group),
        ]

        error_messages = [message for message in messages if message]
        return "\n".join(error_messages)

    @staticmethod
    def __get_has_name_error_message(group):
        has_name = group.name() != ""
        return "" if has_name else "should have a name"

    @staticmethod
    def __name_lowercase_error_message(group):
        is_lowercase = group.name().lower() == group.name()
        return "" if is_lowercase else "name should be all lowercase"

    @staticmethod
    def __get_returns_list_error_message(group):
        returns_list = GroupMetadataValidator.__values_is_a_non_empty_list(group)
        return "" if returns_list else "should return non-empty list"

    @staticmethod
    def __values_is_a_non_empty_list(group):
        is_list = isinstance(group.info(), list)
        is_empty = len(group.info()) == 0
        return is_list and not is_empty

    @staticmethod
    def __get_contains_repeats_message(group):
        repeats = list(group.info())
        uniques = set(repeats)
        [repeats.remove(unique) for unique in uniques]
        repeats = list(map(lambda x: str(x), repeats))
        return GroupMetadataValidator.__get_message("contains repeats: ", repeats)

    @staticmethod
    def __get_contains_non_category_message(group):
        invalids = [
            str(value)
            for value in group._categories
            if GroupMetadataValidator.__is_not_a_category(value)
        ]
        return GroupMetadataValidator.__get_message(
            "contains invalid class: ", invalids
        )

    @staticmethod
    def __get_alphabetical_message(group):
        message = "should be in alphabetical order"
        values = group.info()
        return "" if sorted(values) == values else message

    @staticmethod
    def __get_message(beginning, lst):
        return (beginning + ", ".join(lst)) if len(lst) else ""

    @staticmethod
    def __is_not_a_category(category):
        return category.__base__ != Category
