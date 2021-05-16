import enum
from qual_id.cli_flag import CliFlag

class Flag(enum.Enum):
  COLLECTION = CliFlag("collection", "c")
  PATTERN = CliFlag("pattern", "p")
  FORMAT = CliFlag("format", "f")
  NUMBER = CliFlag("number", "n")
  HELP = CliFlag("help", "h")