class CategoryHelper:
    __disallowed_characters = [" ", "-", "_"]

    @staticmethod
    def get_values_error_message(category):
        returns_list_message = CategoryHelper.get_returns_list_error_message(category)
        repeats_message = CategoryHelper.get_contains_repeats_message(category)
        invalid_strings_message = CategoryHelper.get_contains_invalid_string_message(
            category
        )
        messages = [returns_list_message, repeats_message, invalid_strings_message]
        error_messages = [message for message in messages if message]
        return "\n".join(error_messages)

    @staticmethod
    def get_returns_list_error_message(category):
        returns_list = CategoryHelper.get_values_returns_a_list(category)
        return "" if returns_list else "should return non-empty list"

    @staticmethod
    def get_values_returns_a_list(category):
        is_list = isinstance(category.get_values(), list)
        is_empty = len(category.get_values()) == 0
        return is_list and not is_empty

    @staticmethod
    def get_contains_invalid_string_message(category):
        invalids = [
            value
            for value in category.get_values()
            if CategoryHelper.string_contains_disallowed_character(value)
        ]
        return CategoryHelper.get_message("contains invalid strings: ", invalids)

    @staticmethod
    def get_contains_repeats_message(category):
        repeats = category.get_values()
        uniques = set(category.get_values())
        [repeats.remove(unique) for unique in uniques]
        return CategoryHelper.get_message("contains repeats: ", repeats)

    @staticmethod
    def get_message(beginning, lst):
        return (beginning + ", ".join(lst)) if len(lst) else ""

    @staticmethod
    def string_contains_disallowed_character(str):
        return any([c in str for c in CategoryHelper.__disallowed_characters])
