class CommandFlag:
  def __init__(self, long, short):
      self._long = long
      self._short = short
      self._values = { self._format_long(), self._format_short() }

  def name(self):
    return self._long

  def equals(self, flag):
    return flag in self._values

  def _format_long(self):
      return "--{0}".format(self._long)

  def _format_short(self):
      return "-{0}".format(self._short)
