from qual_id.info.flag import Flag
from qual_id.groups import GroupFactory
from qual_id.groups.all import All

class InfoFactory:
    @staticmethod
    def get(flag, value = None):
        if flag == Flag.GROUP:
            return InfoFactory._group_get(value)
        if flag == Flag.CATEGORY:
            return InfoFactory._category_get(value)
        if flag == Flag.FORMAT:
            return ["json", "csv"]

    @staticmethod
    def has(flag, value):
        if flag == Flag.GROUP:
            return InfoFactory._group_has(value) 
        if flag == Flag.CATEGORY:
            return InfoFactory._category_has(value) 

    @staticmethod
    def _group_get(name):
      if name:
        return GroupFactory.get(name).info()
      return GroupFactory.info()
    
    @staticmethod
    def _category_get(name):
      if name:
        return All.get(name).info()
      return All.info()

    @staticmethod
    def _group_has(name):
        return GroupFactory.has(name)

    @staticmethod
    def _category_has(name):
        return len(All.invalid([name])) == 0
