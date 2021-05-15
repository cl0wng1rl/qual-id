from qual_id.pattern import Pattern
from qual_id.collection_factory import CollectionFactory


class PatternValidator:
    def __init__(self, valid_collection, categories):
        self._collection = valid_collection
        self._categories = categories
        self._is_valid = None
        self._error_message = None

    def validate(self):
        self._is_valid = self._validate_pattern()

    def is_valid(self):
        return self._is_valid

    def error_message(self):
        return self._error_message

    def _validate_pattern(self):
        collection = CollectionFactory.get(self._collection)
        if not (0 < len(self._categories) < 6):
            self._error_message = "number of categories should be between 1 and 5"
            return False
        invalid = collection.invalid(self._categories)
        if invalid:
            self._error_message = "invalid categories: %s" % (invalid)
            return False
        return True
