from .category import Category
import random


class RandomId(Category):
    _name = "randomid"

    @classmethod
    def random(cls):
        return cls.__get_id()

    @classmethod
    def __get_id(cls):
        return "".join([cls.__random_character() for _ in range(10)])

    @classmethod
    def __random_character(cls):
        rand = random.randint(0, 35)
        if rand < 26:
            return cls.__letter(rand)
        return cls.__number(rand)

    @classmethod
    def __letter(cls, order):
        return chr(order + 97)

    @classmethod
    def __number(cls, order):
        return chr(order + 22)
