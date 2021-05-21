from random import choice


class Group:
    _RANDOM_CATEGORY_NAME = "random"

    _name = ""
    _categories = []
    _category_map = {}

    @classmethod
    def name(cls):
        return cls._name

    @classmethod
    def get(cls, category_name):
        if category_name == cls._RANDOM_CATEGORY_NAME:
            return choice(cls._categories)
        return cls._get_category_map().get(category_name)

    @classmethod
    def invalid(cls, category_names):
        return [name for name in category_names if cls._is_invalid(name)]

    @classmethod
    def info(cls):
        return list(map(lambda c: c.name(), cls._categories))

    @classmethod
    def _is_invalid(cls, name):
        is_not_random = name != cls._RANDOM_CATEGORY_NAME
        return (name not in cls._get_category_map()) and (is_not_random)

    @classmethod
    def _get_category_map(cls):
        if not cls._category_map:
            cls._category_map = dict((c.name(), c) for c in cls._categories)
        return cls._category_map
