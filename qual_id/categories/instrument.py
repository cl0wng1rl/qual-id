from ..category import Category


class Instrument(Category):
  def get_values(self):
    return [
        'guitar',
        'bass',
        'drumkit',
        'banjo',
        'cello',
        'violin',
        'ukelele'
    ]
