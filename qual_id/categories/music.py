from ..category import Category


class Music(Category):
    def get_values(self):
        return [
            "rock",
            "metal",
            "blues",
            "jazz",
            "dubstep",
            "funk",
            "techno",
            "house",
            "orchestra",
            "indie",
            "hardcore",
            "kpop",
            "jpop",
            "punk",
        ]
