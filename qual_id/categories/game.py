from ..category import Category


class Game(Category):
  def get_values(self):
    return [
        'basketball',
        'cricket',
        'hockey',
        'chess',
        'tennis',
        'badminton',
        'football',
        'wrestling',
        'rugby',
        'baseball',
        'cycling'
    ]
