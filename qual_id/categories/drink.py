from ..category import Category


class Drink(Category):
    def get_values(self):
        return [
            "beer",
            "coffee",
            "juice",
            "latte",
            "macchiato",
            "milk",
            "smoothie",
            "tea",
            "water",
            "wine",
        ]
