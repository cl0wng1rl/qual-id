from qual_id.cli.helper import Helper as IHelper

class Helper(IHelper):
    HELP_MESSAGE_LINES = [
      " ",
      "Qual ID - get qualitative IDs",
      " ",
      "qual-id --info [parameter] [value?]",
      " ",
      "[parameter]:",
      "  category                         show all category names",
      "  collection                       show all collection names",
      "  format                           show all available formats",
      " ",
      "[parameter] [value]:",
      "  category [category-name]         show all values for a given category",
      "  collection [collection-name]     show all categories in a given collection",
      " ",
    ]
