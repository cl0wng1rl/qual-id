class CliFlag:
  def __init__(self, long, short):
      self._long = long
      self._short = short
      self._values = { self._format_long(), self._format_short() }

  def _format(self, long, short):
    return { self._format_long(), self._format_short() }

  def _format_long(self):
      return "--{0}".format(self._long)

  def _format_short(self):
      return "-{0}".format(self._short)

  def name(self):
    return self._long

  def equals(self, flag):
    return flag in self._values