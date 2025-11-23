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
from InquirerPy import inquirer
from prompt_toolkit.styles import Style
from InquirerPy.base.control import Choice
import questionary
import jatekmestermenu
import pyfiglet
import asciiart_converter
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

def center_option(text: str) -> str:
    return "\n".join(line.center(cols()) for line in text.split("\n"))

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
    ujjatektext = r"""
     ⡇⢸ ⠠   ⠠ ⢀⣀ ⣰⡀ ⢀⡀ ⡇⡠
     ⠣⠜ ⡸   ⡸ ⠣⠼ ⠘⠤ ⠣⠭ ⠏⠢
     """
    
    betoltestext = r"""
     ⣏⡱ ⢀⡀ ⣰⡀ ⢀⡀ ⡇ ⣰⡀ ⢀⡀ ⢀⣀
     ⠧⠜ ⠣⠭ ⠘⠤ ⠣⠜ ⠣ ⠘⠤ ⠣⠭ ⠭⠕
    """
    
    szabalyzattext = r"""
     ⢎⡑ ⣀⣀ ⢀⣀ ⣇⡀ ⢀⣀ ⡇ ⡀⢀ ⣀⣀ ⢀⣀ ⣰⡀
     ⠢⠜ ⠴⠥ ⠣⠼ ⠧⠜ ⠣⠼ ⠣ ⣑⡺ ⠴⠥ ⠣⠼ ⠘⠤
    """
    
    vilagtext = r"""
     ⡇⢸ ⠄ ⡇ ⢀⣀ ⢀⡀ ⢀⡀ ⡇⡠
     ⠸⠃ ⠇ ⠣ ⠣⠼ ⣑⡺ ⠣⠜ ⠏⠢
     """
    
    options = [ujjatektext, betoltestext, szabalyzattext, vilagtext]
    
    centered_options = [center_option(opt) for opt in options]
    cls()
    asciiras(cim, "white")
    choice = inquirer.select(
        message = "",
        pointer = "",
        choices = centered_options,
        multiselect = False
    
    ).execute()
    print(choice)
    print(ujjatektext)
    if choice == centered_options[0]:
        print("az alma menno")
        vilagvalaszto()
        



def vilagvalaszto():  
    cls()
    options=[]                                                            
    cim = [
" __ __  ____  _       ____   ____   ___   __  _  ",
"|  |  ||    || |     /    | /    | /   \ |  |/ ] ",
"|  |  | |  | | |    |  o  ||   __||     ||  ' /  ",
"|  |  | |  | | |___ |     ||  |  ||  O  ||    \  ",
"|  :  | |  | |     ||  _  ||  |_ ||     ||     \ ",
" \   /  |  | |     ||  |  ||     ||     ||  .  | ",
"  \_/  |____||_____||__|__||___,_| \___/ |__|\_| "
                                           
    ]
    asciiras(cim, "white")
    print("\n" * 3)
    cls()
    asciiras(asciiart_converter.text_to_ascii("1 heloszia"), "red")
    asciiras(asciiart_converter.text_to_ascii("2 HELOSZIA"), "blue")
    asciiras(asciiart_converter.text_to_ascii("3 HELOszia"), "green")
    input("")
    


def jatekmode():
    print("nehezseg")
    print("DLC")


################################
#vasárnap
def meglevo():
    print("regi harc")