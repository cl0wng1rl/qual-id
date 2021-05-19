from qual_id.cli.info.flag import Flag
from qual_id.collections import CollectionFactory
from qual_id.collections.all import All

class InfoFactory:
    @staticmethod
    def get(parameter, value = None):
        if parameter == Flag.COLLECTION:
            return InfoFactory._collection_get(value)
        if parameter == Flag.CATEGORY:
            return InfoFactory._category_get(value)
        if parameter == Flag.FORMAT:
            return ["json", "csv"]

    @staticmethod
    def has(parameter, value):
        if parameter == Flag.COLLECTION:
            return InfoFactory._collection_has(value) 
        if parameter == Flag.CATEGORY:
            return InfoFactory._category_has(value) 

    @staticmethod
    def _collection_get(name):
      if name:
        return CollectionFactory.get(name).info()
      return CollectionFactory.info()
    
    @staticmethod
    def _category_get(name):
      if name:
        return All.get(name).info()
      return All.info()

    @staticmethod
    def _collection_has(name):
        return CollectionFactory.has(name)

    @staticmethod
    def _category_has(name):
        return len(All.invalid([name])) == 0
