from ..category import Category


class Music(Category):
    def get_values(self):
        return [
            "blues",
            "dubstep",
            "funk",
            "hardcore",
            "house",
            "indie",
            "jazz",
            "jpop",
            "kpop",
            "metal",
            "orchestra",
            "punk",
            "rock",
            "techno",
        ]
