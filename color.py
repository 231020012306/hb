import colorama

MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def color_print(text: str, *effects: str):
    """
    MAgic will happen
    :param text: The text to print
    :param effect: The effects we want
    """
    output_string="{0}{1}".format(color_print(),effects,text)
    print(output_string)


colorama.init()
color_print("Tommorow will be our", UNDERLINE)
color_print("one of the special days",BOLD)
color_print("BEST WISHES TO US",MAGENTA )
colorama.deinit()
