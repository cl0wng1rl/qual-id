from .collections import *

class CollectionFactory:
    _collections = [All.get_instance(), Minimal.get_instance(), Neutral.get_instance()]
    _collection_map = dict((c.name(), c) for c in _collections)
    
    @staticmethod
    def get(name):
        return CollectionFactory._collection_map.get(name)

    @staticmethod
    def has(name):
        return name in CollectionFactory._collection_map
