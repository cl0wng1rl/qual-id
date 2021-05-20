import enum
from qual_id.cli.info.info_flag import InfoFlag

class Flag(enum.Enum):
  GROUP = InfoFlag("group", "g")
  CATEGORY = InfoFlag("category", "c")
  FORMAT = InfoFlag("format", "f", True)

  @staticmethod
  def from_string(string):
      return next((flag for flag in Flag if flag.value.equals(string)), None)