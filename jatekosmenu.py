import os
import keyboard
import cards
import fileread
import kazamata
import time
from termcolor import colored, cprint
import kazamata
import fight
import sys
import msvcrt

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def cols():
    return os.get_terminal_size().columns

def rows():
    return os.get_terminal_size().lines

def asciiras(s,color):
    for line in s:
        cprint(line.center(cols()),f"{color}")


def clear_input_field():
    while msvcrt.kbhit():
        msvcrt.getch()

def jatekosmenu():
    cim = [
"  ____   ____  ______    ___  __  _   ___   _____",
" |    | /    ||      |  /  _]|  |/ ] /   \ / ___/",
" |__  ||  o  ||      | /  [_ |  ' / |     (   \_ ",
" __|  ||     ||_|  |_||    _]|    \ |  O  |\__  |",
"/  |  ||  _  |  |  |  |   [_ |     ||     |/  \ |",
"\  `  ||  |  |  |  |  |     ||  .  ||     |\    |",
" \____j|__|__|  |__|  |_____||__|\_| \___/  \___|"

    ]
    ujjatektext = [
    " ⡇⢸ ⠠   ⠠ ⢀⣀ ⣰⡀ ⢀⡀ ⡇⡠"
    " ⠣⠜ ⡸   ⡸ ⠣⠼ ⠘⠤ ⠣⠭ ⠏⠢"
    ]


 
    print("2. Betoltes")
    print("3. Szabályzat")
    print("4. világok")


def vilagvalaszto():                                                                                 
    print("vilagok felsorolva")


def jatekmode():
    print("nehezseg")
    print("DLC")


################################
#vasárnap
def meglevo():
    print("regi harc")