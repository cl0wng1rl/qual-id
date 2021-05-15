from qual_id.collection_factory import CollectionFactory


class CollectionValidator:
    def __init__(self, collection):
        self._collection = collection
        self._is_valid = None
        self._error_message = None

    def validate(self):
        self._is_valid = CollectionFactory.has(self._collection)
        if not self._is_valid:
            self._error_message = "invalid collection: %s" % (self._collection)

    def is_valid(self):
        return self._is_valid

    def error_message(self):
        return self._error_message
