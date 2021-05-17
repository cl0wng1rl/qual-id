from qual_id.categories.category import Category

class CollectionMetadataValidator:
    __disallowed_characters = [" ", "-", "_", "&"]

    @staticmethod
    def validate(collection):
        messages = [
            CollectionMetadataValidator.__get_has_name_error_message(collection),
            CollectionMetadataValidator.__name_lowercase_error_message(collection),
            CollectionMetadataValidator.__get_returns_list_error_message(collection),
            CollectionMetadataValidator.__get_contains_repeats_message(collection),
            CollectionMetadataValidator.__get_contains_non_category_message(collection),
            CollectionMetadataValidator.__get_alphabetical_message(collection),
        ]

        error_messages = [message for message in messages if message]
        return "\n".join(error_messages)

    @staticmethod
    def __get_has_name_error_message(collection):
        has_name = collection.name() != ""
        return "" if has_name else "should have a name"

    @staticmethod
    def __name_lowercase_error_message(collection):
        is_lowercase = collection.name().lower() == collection.name()
        return "" if is_lowercase else "name should be all lowercase"

    @staticmethod
    def __get_returns_list_error_message(collection):
        returns_list = CollectionMetadataValidator.__values_is_a_non_empty_list(collection)
        return "" if returns_list else "should return non-empty list"

    @staticmethod
    def __values_is_a_non_empty_list(collection):
        is_list = isinstance(collection._categories, list)
        is_empty = len(collection._categories) == 0
        return is_list and not is_empty

    @staticmethod
    def __get_contains_repeats_message(collection):
        repeats = list(collection._categories)
        uniques = set(repeats)
        [repeats.remove(unique) for unique in uniques]
        repeats = list(map(lambda x: str(x), repeats))
        return CollectionMetadataValidator.__get_message("contains repeats: ", repeats)

    @staticmethod
    def __get_contains_non_category_message(collection):
        invalids = [
            str(value)
            for value in collection._categories
            if CollectionMetadataValidator.__is_not_a_category(value)
        ]
        return CollectionMetadataValidator.__get_message(
            "contains invalid class: ", invalids
        )

    @staticmethod
    def __get_alphabetical_message(collection):
        message = "should be in alphabetical order"
        values = list(map(lambda x: x.name(), collection._categories))
        return "" if sorted(values) == values else message

    @staticmethod
    def __get_message(beginning, lst):
        return (beginning + ", ".join(lst)) if len(lst) else ""

    @staticmethod
    def __is_not_a_category(category):
        return category.__base__ != Category
