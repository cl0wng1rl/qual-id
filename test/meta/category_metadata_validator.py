class CategoryMetadataValidator:
    __disallowed_characters = [" ", "-", "_", "&"]

    @staticmethod
    def validate(category):
        messages = [
            CategoryMetadataValidator.__get_has_name_error_message(category),
            CategoryMetadataValidator.__name_lowercase_error_message(category),
            CategoryMetadataValidator.__get_returns_list_error_message(category),
            CategoryMetadataValidator.__get_contains_repeats_message(category),
            CategoryMetadataValidator.__get_contains_invalid_string_message(category),
            CategoryMetadataValidator.__get_alphabetical_message(category),
            CategoryMetadataValidator.__get_contains_uppercase_string_message(category),
        ]

        error_messages = [message for message in messages if message]
        return "\n".join(error_messages)

    @staticmethod
    def __get_has_name_error_message(category):
        has_name = category.name() != ""
        return "" if has_name else "should have a name"

    @staticmethod
    def __name_lowercase_error_message(category):
        is_lowercase = category.name().lower() == category.name()
        return "" if is_lowercase else "name should be all lowercase"

    @staticmethod
    def __get_returns_list_error_message(category):
        returns_list = CategoryMetadataValidator.__values_is_a_non_empty_list(category)
        return "" if returns_list else "should return non-empty list"

    @staticmethod
    def __values_is_a_non_empty_list(category):
        is_list = isinstance(category._values, list)
        is_empty = len(category._values) == 0
        return is_list and not is_empty

    @staticmethod
    def __get_contains_repeats_message(category):
        repeats = list(category._values)
        uniques = set(repeats)
        [repeats.remove(unique) for unique in uniques]
        return CategoryMetadataValidator.__get_message("contains repeats: ", repeats)

    @staticmethod
    def __get_contains_invalid_string_message(category):
        invalids = [
            value
            for value in category._values
            if CategoryMetadataValidator.__string_contains_disallowed_character(value)
        ]
        return CategoryMetadataValidator.__get_message(
            "contains invalid strings: ", invalids
        )

    @staticmethod
    def __get_alphabetical_message(category):
        message = "should be in alphabetical order"
        values = category._values
        return "" if sorted(values) == values else message

    @staticmethod
    def __get_contains_uppercase_string_message(category):
        invalids = [
            value
            for value in category._values
            if CategoryMetadataValidator.__string_contains_uppercase_character(value)
        ]
        return CategoryMetadataValidator.__get_message(
            "contains uppercase strings: ", invalids
        )

    @staticmethod
    def __get_message(beginning, lst):
        return (beginning + ", ".join(lst)) if len(lst) else ""

    @staticmethod
    def __string_contains_disallowed_character(str):
        return any(
            [c in str for c in CategoryMetadataValidator.__disallowed_characters]
        )

    @staticmethod
    def __string_contains_uppercase_character(str):
        return any([c for c in list(str) if c.isupper()])
