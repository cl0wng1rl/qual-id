from ..category import Category

class Company(Category):
  def get_values(self):
    return [
        "agriculture",
        "art",
        "construction",
        "corporate",
        "finance",
        "government",
        "manufacturing",
        "media",
        "medical",
        "service",
        "transportation"
    ]
