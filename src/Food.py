from .Category import Category

class Food(Category):
  def get_values(self):
    return [
      'apple',
      'chocolate',
      'cookie',
      'egg',
      'ham',
      'lemon'
    ]