from qual_id.cli.helper import Helper as IHelper

class Helper(IHelper):
    HELP_MESSAGE_LINES = [
      " ",
      "Qual ID - get qualitative IDs",
      " ",
      "qual-id --info [flag] [value?]",
      " ",
      "[flag]:",
      "-c, --category                  show all category names",
      "-g, --group                     show all group names",
      "-f, --format                    show all available formats",
      " ",
      "[flag] [value]:",
      "--category [category-name]     show all values for a given category",
      "--group    [group-name]        show all categories in a given group",
      " ",
    ]
