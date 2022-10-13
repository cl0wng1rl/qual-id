from .category import Category
import random

CHAR_MAP = {
    "a": "bcdfghjklmnpqrstuvwxyz",
    "b": "aeiloruy",
    "c": "aehiloruy",
    "d": "aeiloruy",
    "e": "abcdefghjklmnopqrstvwxyz",
    "f": "aeiloruy",
    "g": "aeiloruy",
    "h": "aeiouy",
    "i": "abcdfgklmnoprstvxz",
    "j": "aeiou",
    "k": "aeiloruy",
    "l": "aeiouy",
    "m": "aeiouy",
    "n": "aeiouy",
    "o": "abcdefghijklmnopqrstuvwxyz",
    "p": "aeiloruy",
    "q": "aeiou",
    "r": "aeiouy",
    "s": "acehiklmnopqtuwy",
    "t": "aeiloruy",
    "u": "abcdefghjklmnopqrstvwxz",
    "v": "aeiouy",
    "w": "aeiouy",
    "x": "aeiouy",
    "y": "aeiou",
    "z": "aeiouy",
    "_": "abcdefghijklmnopqrstuvwxyz",
}


class Gibberish(Category):
    _name = "gibberish"

    @classmethod
    def random(cls):
        return cls._get_string_of_length(random.randint(5, 10))

    @classmethod
    def _get_string_of_length(cls, length):
        c, str = "_", ""
        for _ in range(length):
            c = cls._random_next_character(c)
            str += c
        return str

    @classmethod
    def _random_next_character(cls, letter):
        return random.choice(CHAR_MAP[letter])
