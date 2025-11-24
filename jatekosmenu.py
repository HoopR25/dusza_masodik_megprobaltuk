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
import jatekmestermenu
import asciiart_converter
from InquirerPy.base.control import Choice
from InquirerPy.utils import color_print
from InquirerPy import get_style

import math

theme = get_style({
    "questionmark": "#000000",
    "answermark": "#b10101",
    "input": "#420101",
    "question": "",
    "answered_question": "#141514",
    "pointer": "#b70000",
    "instruction": "#000000",
    "long_instruction": "#000000",
    "answer": "#000000 bold",
    "long_answer": "#000000",
    "separator": "",
    "selected": "#000000",
    "marker": "#000000",
    "disabled": "gray italic"
})


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
" \____||__|__|  |__|  |_____||__|\_| \___/  \___|"

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
    
    vilagtext =r"""
     ⡇⢸ ⠄ ⡇ ⢀⣀ ⢀⡀ ⢀⡀ ⡇⡠
     ⠸⠃ ⠇ ⠣ ⠣⠼ ⣑⡺ ⠣⠜ ⠏⠢
     """
    
    options = [ujjatektext, betoltestext, szabalyzattext, vilagtext]
    
    centered_options = [
    center_option(ujjatektext),
    center_option(betoltestext),
    center_option(szabalyzattext),
    center_option(vilagtext)
]

    cls()
    asciiras(cim, "white")
    choice = inquirer.select(
        message = "",
        pointer = "",
        choices = centered_options,
        multiselect = False,
        style = theme
    
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
    vilagok = jatekmestermenu.vilagok.copy()
    opciok = [[]]
    for i in range(math.ceil(len(vilagok) / 3)):
        opciok.append([])
    for i in range(math.ceil(len(vilagok) / 3)):
        if len(vilagok) - (i * 3) <= 3:
            if i != 0:
                opciok[i].append(center_option(asciiart_converter.text_to_ascii("Elozo oldal", 1)))
                for j in range(i * 3, len(vilagok)):
                    opciok[i].append(center_option(asciiart_converter.text_to_ascii(vilagok[j][0], 1)))
            else:
                for j in range(i * 3, len(vilagok)):
                    opciok[i].append(center_option(asciiart_converter.text_to_ascii(vilagok[j][0], 1)))
        elif i == 0:
            for j in range(i * 3,(i * 3) + 3):
                opciok[i].append(center_option(asciiart_converter.text_to_ascii(vilagok[j][0], 1)))
            opciok[i].append(center_option(asciiart_converter.text_to_ascii("Kovetkezo oldal", 1)))
        else:
            opciok[i].append(center_option(asciiart_converter.text_to_ascii("Elozo oldal", 1)))
            for j in range(i * 3,(i * 3) + 3):
                opciok[i].append(center_option(asciiart_converter.text_to_ascii(vilagok[j][0], 1)))
            opciok[i].append(center_option(asciiart_converter.text_to_ascii("Kovetkezo oldal", 1)))
    oldalszam = 1
    maxoldalszam = math.ceil(len(vilagok) / 3)
    elozotext = center_option(asciiart_converter.text_to_ascii("Elozo oldal", 1))
    kovetkezotext = center_option(asciiart_converter.text_to_ascii("Kovetkezo oldal", 1))
    while True: 
        cls()
        asciiras(cim, "white")
        print("\n" * 5)
        choice = inquirer.select(
            message = center_option(f"{oldalszam}/{maxoldalszam}"),
            pointer = "",
            choices = opciok[oldalszam - 1],
            multiselect = False,
            style = theme
        ).execute()
        
        if choice == elozotext:
            oldalszam -= 1
        elif choice == kovetkezotext:
            oldalszam += 1
        else:
            break
    
    
    input("")
    

# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
# ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! LEMENTENI JATEKOT: VILAGNEV, GYUJTEMENY, GYUJTSTATS, BEALLITASOK

def jatekmode():
    print("nehezseg")
    print("DLC")


################################
#vasárnap
def meglevo():
    print("regi harc")