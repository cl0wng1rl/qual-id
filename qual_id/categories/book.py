from ..category import Category

class Book(Category):
  def get_values(self):
    return [
        'Art',
        'music',
        'business',
        'comic',
        'technology',
        'cooking',
        'entertaiment',
        'education',
        'history',
        'kids',
        'literature',
        'medical',
        'romance',
        'sport',
        'religion'
    ]
