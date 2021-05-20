from qual_id.cli.helper import Helper as IHelper

class Helper(IHelper):
    HELP_MESSAGE_LINES = [
        " ",
        "Qual ID - get qualitative IDs",
        " ",
        "qual-id [options]",
        " ",
        "options:",
        "-h, --help                show brief help",
        "-p, --pattern             specify the pattern of the qual IDs",
        "-g, --group               specify which group to use",
        "-n, --number              specify how many qual IDs to receive",
        "-f, --format              specify the format of the qual IDs",
        " ",
    ]
