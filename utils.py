import os


def clear_console():
    """
    Очистка консоли
    """
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
