from qual_id.category_map import CategoryMap


class CategoryMapFactory:
    @staticmethod
    def get(str):
        keys = CategoryMapFactory.__name_to_keys[str] if str else []
        return CategoryMap(keys)

    @staticmethod
    def has(str):
        return (str in CategoryMapFactory.__name_to_keys) or str == ""

    __name_to_keys = {
        "minimal": [
            "adjective",
            "animal",
            "bird",
            "color",
            "food",
            "fruit",
            "geography",
            "instrument",
            "planet",
            "tea",
            "vehicle",
        ],
        "neutral": [
            "adjective",
            "animal",
            "bird",
            "capital",
            "city",
            "clothing",
            "color",
            "constellation",
            "country",
            "currency",
            "drink",
            "element",
            "emotion",
            "food",
            "fruit",
            "geography",
            "instrument",
            "particle",
            "planet",
            "state",
            "tea",
            "tool",
            "utensil",
            "vehicle",
            "wine",
        ],
    }
