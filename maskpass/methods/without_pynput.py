# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 05:16:41 2021

@author: FuturisticGoo
"""

#from maskpass.input_methods.cross_getch import CrossGetch

try:
    from .cross_getch import CrossGetch
except ImportError:
    from cross_getch import CrossGetch


def askpass(prompt="Enter Password: ", mask="*"):
    """
    Description
    ----------
    A simple function which can be used for asking password

    Parameters
    ----------
    prompt : String, optional
        DESCRIPTION. The default is "Enter Password: ".

    mask : String, optional
        DESCRIPTION. Masks the input password.
                     The default is "*", "" can be used for
                     no masking like in Unix passwords.
                     Single length string preferred, multi length string works.
    Raises
    ------
    KeyboardInterrupt
        When CTRL+C pressed while typing the password

    Returns
    -------
    Returns the entered password in string format.
    Returns empty string "" if ESC pressed

    """

    password_input = ""
    count = 0
    cross_getch = CrossGetch()

    print(prompt, end="", flush=True)

    while True:
        char = cross_getch.getch()
        try:
            char = char.decode("utf-8")
        except UnicodeDecodeError:
            None
        else:
            if char == "\x0D":
                # ENTER key
                break
            elif char in ["\x08", "\x7F"]:
                if count != 0:
                    print("\b \b"*len(mask), end="", flush=True)
                    count -= 1
                password_input = password_input[:-1]
            else:
                print(mask, end="", flush=True)
                if mask != "":
                    count += 1
                password_input += char
    print(flush=True)
    return password_input
