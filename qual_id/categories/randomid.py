from ..category import Category
import random


class RandomId(Category):
    def get_values(self):
        return [self.__get_id()]

    def __get_id(self):
        return "".join([self.__random_character() for _ in range(10)])

    def __random_character(self):
        rand = random.randint(0, 35)
        if rand < 26:
            return self.__letter(rand)
        return self.__number(rand)

    def __letter(self, order):
        return chr(order + 97)

    def __number(self, order):
        return chr(order + 22)