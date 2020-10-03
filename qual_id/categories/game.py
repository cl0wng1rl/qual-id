from ..category import Category


class Game(Category):
    def get_values(self):
        return [
            "badminton",
            "baseball",
            "basketball",
            "chess",
            "cricket",
            "cycling",
            "football",
            "hockey",
            "rugby",
            "tennis",
            "wrestling",
        ]
