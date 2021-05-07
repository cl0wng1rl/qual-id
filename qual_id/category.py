from random import choice


class Category:
    _name = ""
    _values = [""]

    @classmethod
    def random(cls):
        return choice(cls._values)

    @classmethod
    def get_name(cls):
        return cls._name
