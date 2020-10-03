from ..category import Category


class Emotion(Category):
    def get_values(self):
        return [
            "admiration",
            "amusement",
            "anger",
            "boredom",
            "disgust",
            "envy",
            "fear",
            "hatred",
            "joy",
            "love",
            "relief",
            "sadness",
            "surprise",
        ]
