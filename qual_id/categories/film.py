from ..category import Category


class Film(Category):
    def get_values(self):
        return [
            "action",
            "comedy",
            "crime",
            "drama",
            "fantasy",
            "horror",
            "mystery",
            "romance",
            "thriller",
            "western",
        ]
