class CategoryHelper:
    __disallowed_characters = [" ", "-", "_", "&"]

    @staticmethod
    def get_values_error_message(category):
        messages = [
            CategoryHelper.__get_returns_list_error_message(category),
            CategoryHelper.__get_contains_repeats_message(category),
            CategoryHelper.__get_contains_invalid_string_message(category),
            CategoryHelper.__get_alphabetical_message(category),
            CategoryHelper.__get_contains_uppercase_string_message(category),
        ]

        error_messages = [message for message in messages if message]
        return "\n".join(error_messages)

    @staticmethod
    def __get_returns_list_error_message(category):
        returns_list = CategoryHelper.__get_values_returns_a_list(category)
        return "" if returns_list else "should return non-empty list"

    @staticmethod
    def __get_values_returns_a_list(category):
        is_list = isinstance(category.get_values(), list)
        is_empty = len(category.get_values()) == 0
        return is_list and not is_empty

    @staticmethod
    def __get_contains_invalid_string_message(category):
        invalids = [
            value
            for value in category.get_values()
            if CategoryHelper.__string_contains_disallowed_character(value)
        ]
        return CategoryHelper.__get_message("contains invalid strings: ", invalids)

    @staticmethod
    def __get_contains_repeats_message(category):
        repeats = category.get_values()
        uniques = set(repeats)
        [repeats.remove(unique) for unique in uniques]
        return CategoryHelper.__get_message("contains repeats: ", repeats)

    @staticmethod
    def __get_alphabetical_message(category):
        message = "should be in alphabetical order"
        values = category.get_values()
        return "" if sorted(values) == values else message

    @staticmethod
    def __get_contains_uppercase_string_message(category):
        invalids = [
            value
            for value in category.get_values()
            if CategoryHelper.__string_contains_uppercase_character(value)
        ]
        return CategoryHelper.__get_message("contains uppercase strings: ", invalids)

    @staticmethod
    def __get_message(beginning, lst):
        return (beginning + ", ".join(lst)) if len(lst) else ""

    @staticmethod
    def __string_contains_disallowed_character(str):
        return any([c in str for c in CategoryHelper.__disallowed_characters])

    @staticmethod
    def __string_contains_uppercase_character(str):
        return any([c for c in list(str) if c.isupper()])
