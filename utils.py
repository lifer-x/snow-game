import os
def clear_console():
    if os.name=="posix":
        os.system("clear")
    elif os.name=="nt":
        os.system("cls")
clear_console()