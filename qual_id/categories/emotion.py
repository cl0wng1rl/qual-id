from ..category import Category


class Emotion(Category):
    def get_values(self):
        return[
            'joy', 
            'fear', 
            'anger', 
            'sadness',
            'disgust', 
            'envy', 
            'love', 
            'hatred', 
            'admiration', 
            'amusement', 
            'boredom', 
            'relief', 
            'surprise'
        ]
