from ..category import Category


class Film(Category):
    def get_values(self):
        return [
            "action",
            "adventure",
            "animated",
            "comedy",
            "crime",
            "documentary",
            "drama",
            "fantasy",
            "fiction",
            "historical",
            "horror",
            "musical",
            "mystery",
            "romance",
            "silent",
            "sports",
            "supernatural",
            "thriller",
            "war",
            "western",
        ]
