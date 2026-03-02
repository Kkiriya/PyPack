# Author: Émile
# Date: 2026-03-02

# --- Imports --- #
from colorama import Fore, Back, Style, init
init(autoreset=True)

# --- Global Variables --- #
colours = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "reset": Fore.RESET
    }

# --- Stateless Functions --- #
def printHead(str:str, dash_or_equal:bool=True):
    """Prints a given string with surrounding '---' or '==='

    **dash_or_equal:**
        - True: '---'
        - False: '==='

    Args:
        str (str): given str
        dash_or_equal (bool): Default = True
    """
    if dash_or_equal:
        print("--- " + str + " ---")
    else:
        print("=== " + str + " ===")

def printCol(str:str, col:str):
    """Prints a given string in the given colour\n
    **Supported Colours:**
        - Black
        - Red
        - Green
        - Yellow
        - Blue
        - Magenta
        - Cyan
        - White
        - Reset

    Args:
        str (str): given str
        col (str): given colour
    """
    col = col.lower().strip()
    if col not in colours:
        printErr("Colour not supported or mispelled")
        return None

    print(colours[col] + str)

def printColHead(str:str, col:str, dash_or_equal:bool=True):
    """Prints a given string with surrounding '---' or '===' and in the given colour

    **dash_or_equal:**
        - True: '---'
        - False: '==='

    Args:
        str (str): given str
        dash_or_equal (bool): Default = True
        col (str): given colour
    """
    if dash_or_equal:
        printCol(("--- " + str + " ---"), col)

    else:
        printCol(("=== " + str + " ==="), col)

def printHigh(str:str):
    """Prints a given str with a yellow background

    Args:
        msg (str): given str
    """
    print(Back.YELLOW + Style.BRIGHT + str)

def printErr(msg:str):
    """Prints the given message in red with the 'ERROR:' prefix

    Args:
        msg (str): given msg
    """
    print(Fore.WHITE + Back.RED + "ERROR:" + msg)

def printSuc(msg:str):
    """Prints the given message in green with the 'SUCCESS:' prefix

    Args:
        msg (str): given msg
    """
    print(Fore.GREEN + "SUCCESS: " + msg)

# --- Testing the func --- #
def main():
    printHead("Title Message")
    printHead("Title Message", False)
    printCol("Colour Message", "Cyan")
    printColHead("Coloured Title Message", "Blue")
    printColHead("Coloured Title Message", "Blue", False)
    printHigh("Highlighted Message")
    printErr("Error Message")
    printSuc("Success Message")

if __name__ == "__main__":
    main()
