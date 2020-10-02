from ..category import Category


class Drink(Category):
    def get_values(self):
        return [
            "juice",
            "milk",
            "beer",
            "water",
            "coffee",
            "tea",
            "wine",
            "chocolate",
            "ice",
            "smoothie",
            "latte",
            "macchiato",
        ]
