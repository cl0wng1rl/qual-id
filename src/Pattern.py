class Pattern:
  category_map = {
    "animal": "data/animal.txt",
    "food": "data/food.txt",
  }

  def __init__(self, pattern_string):
    self.categories = pattern_string.split('-')

  def is_valid(self):
    if not (0 < len(self.categories) < 6):
      return False
    for category in self.categories:
      path = Pattern.category_map[category]
      if not path:
        return False
    return True
  
  def get_paths(self):
    return [Pattern.category_map[category] for category in self.categories]