from random import choice


class Category:
  def get_random_value(self):
    return choice(self.get_values())

  def get_values(self):
    return ['']
