from ..category import Category

class Company(Category):
  def get_values(self):
    return [
        'agriculture',
        'art',
        'construction',
        'corporate',
        'medical',
        'service',
        'transportation',
        'finance',
        'government',
        'media',
        'manufacturing'
    ]
