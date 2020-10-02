from ..category import Category


class Book(Category):
    def get_values(self):
        return [
            "art",
            "business",
            "comic",
            "cooking",
            "education",
            "entertaiment",
            "history",
            "kids",
            "literature",
            "medical",
            "music",
            "religion",
            "romance",
            "sport",
            "technology",
        ]
