from ..category import Category

class Film(Category):
  def get_values(self):
    return [
        'action',
        'comedy',
        'drama',
        'horror',
        'crime',
        'thriller',
        'mystery',
        'romance',
        'western',
        'fantasy'
    ]
