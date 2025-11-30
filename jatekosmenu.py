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
import game_mode
import math
import mentesek_fileread
import uj_gamemode
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

hardcore = False
kepesseg = False
nehezsegiszint = 0

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
        vilagvalaszto()
    if choice == centered_options[1]:
        betoltes()

def betoltes():
    cls()
    cim = [
" ____     ___ ______   ___   _     ______    ___  _____",
"|    \   /  _]      | /   \ | |   |      |  /  _]/ ___/",
"|  o  ) /  [_|      ||     || |   |      | /  [_(   \_ ",
"|     ||    _]_|  |_||  O  || |___|_|  |_||    _]\__  |",
"|  O  ||   [_  |  |  |     ||     | |  |  |   [_ /  \ |",
"|     ||     | |  |  |     ||     | |  |  |     |\    |",
"|_____||_____| |__|   \___/ |_____| |__|  |_____| \___|"
    ]
    asciiras(cim,"white")
    opciok = [[]]
    vilagok = mentesek_fileread.mentesek
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
    uj_gamemode.JATEK(asciiart_converter.ascii_to_text(choice))

def vilagvalaszto():  
    cls()           
    global nehezsegiszint
    global hardcore
    global kepesseg           
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
    hardcore = False
    kepesseg = False
    nehezsegiszint = 0
    beallitasok(asciiart_converter.ascii_to_text(choice))
    
    
    

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



def beallitasok(vilagnev):
    cls()
    cim = [
    " ____     ___   ____  _      _      ____  ______   ____  _____  ___   __  _  ",
    "|    \   /  _] /    || |    | |    |    ||      | /    |/ ___/ /   \ |  |/ ] ",
    "|  o  ) /  [_ |  o  || |    | |     |  | |      ||  o  (   \_ |     ||  ' /  ",
    "|     ||    _]|     || |___ | |___  |  | |_|  |_||     |\__  ||  O  ||    \  ",
    "|  O  ||   [_ |  _  ||     ||     | |  |   |  |  |  _  |/  \ ||     ||     \ ",
    "|     ||     ||  |  ||     ||     | |  |   |  |  |  |  |\    ||     ||  .  | ",
    "|_____||_____||__|__||_____||_____||____|  |__|  |__|__| \___| \___/ |__|\_| "
                                                                     ]
    utasitas = [
     "⣎⣱ ⢀⣸ ⠠ ⢀⣀   ⣀⣀  ⢀⡀ ⢀⡀   ⢀⣀   ⣀⡀ ⢀⡀ ⣇⡀ ⢀⡀ ⣀⣀ ⢀⣀ ⢀⡀ ⢀⡀ ⠄   ⢀⣀ ⣀⣀ ⠄ ⣀⡀ ⣰⡀ ⢀⡀ ⣰⡀",
     "⠇⠸ ⠣⠼ ⡸ ⠣⠼   ⠇⠇⠇ ⠣⠭ ⣑⡺   ⠣⠼   ⠇⠸ ⠣⠭ ⠇⠸ ⠣⠭ ⠴⠥ ⠭⠕ ⠣⠭ ⣑⡺ ⠇   ⠭⠕ ⠴⠥ ⠇ ⠇⠸ ⠘⠤ ⠣⠭ ⠘⠤"
    ]
    utasitas2 = [
     "⣎⣵ ⣰⡀ ⢀⡀ ⡇   ⢺  ⣎⣵ ⠄ ⢀⡀",
     "⠫⠜ ⠘⠤ ⠣⠜ ⠣   ⠼⠄ ⠫⠜ ⠇ ⣑⡺"
    ]
    opt1 = r"""
     ⡷⣸ ⢀⡀ ⣇⡀ ⢀⡀ ⣀⣀ ⢀⣀ ⢀⡀ ⢀⡀ ⠄   ⢀⣀ ⣀⣀ ⠄ ⣀⡀ ⣰⡀
     ⠇⠹ ⠣⠭ ⠇⠸ ⠣⠭ ⠴⠥ ⠭⠕ ⠣⠭ ⣑⡺ ⠇   ⠭⠕ ⠴⠥ ⠇ ⠇⠸ ⠘⠤
    """
    opt2 = r"""
    ⣇⣸ ⢀⣀ ⡀⣀ ⢀⣸ ⢀⣀ ⢀⡀ ⡀⣀ ⢀⡀
    ⠇⠸ ⠣⠼ ⠏  ⠣⠼ ⠣⠤ ⠣⠜ ⠏  ⠣⠭
    """
    opt3 = r"""
     ⣇⠜ ⢀⡀ ⣀⡀ ⢀⡀ ⢀⣀ ⢀⣀ ⢀⡀ ⢀⡀
     ⠇⠱ ⠣⠭ ⡧⠜ ⠣⠭ ⠭⠕ ⠭⠕ ⠣⠭ ⣑⡺
    """
    opt4 = r"""
     ⢎⡑ ⣰⡀ ⢀⣀ ⡀⣀ ⣰⡀
     ⠢⠜ ⠘⠤ ⠣⠼ ⠏  ⠘⠤
    """
    opt5 = r"""
     ⡇⢸ ⠄ ⢀⣀ ⢀⣀ ⣀⣀ ⢀⣀
     ⠸⠃ ⠇ ⠭⠕ ⠭⠕ ⠴⠥ ⠣⠼
    """
    options = [
    center_option(opt5),
    center_option(opt1),
    center_option(opt2),
    center_option(opt4)
    ]
    
    #while not nehezsegiszint.isdigit():
    while True:
        cls()
        asciiras(cim,"white")
        
        choice = inquirer.select(
                message = "",
                pointer = "",
                choices = options,
                multiselect = False,
                style = theme
            ).execute()
        if choice == options[0]:
            vilagvalaszto()
            break
        elif choice == options[1]:
            nehezseg()
        elif choice == options[2]:
            hardcore1()
        elif choice == options[3]:
            nev(vilagnev)

def nehezseg():
    cls()
    global nehezsegiszint
    utasitas = [
     "⣎⣱ ⢀⣸ ⠠ ⢀⣀   ⣀⣀  ⢀⡀ ⢀⡀   ⢀⣀   ⣀⡀ ⢀⡀ ⣇⡀ ⢀⡀ ⣀⣀ ⢀⣀ ⢀⡀ ⢀⡀ ⠄   ⢀⣀ ⣀⣀ ⠄ ⣀⡀ ⣰⡀ ⢀⡀ ⣰⡀",
     "⠇⠸ ⠣⠼ ⡸ ⠣⠼   ⠇⠇⠇ ⠣⠭ ⣑⡺   ⠣⠼   ⠇⠸ ⠣⠭ ⠇⠸ ⠣⠭ ⠴⠥ ⠭⠕ ⠣⠭ ⣑⡺ ⠇   ⠭⠕ ⠴⠥ ⠇ ⠇⠸ ⠘⠤ ⠣⠭ ⠘⠤"
    ]
    utasitas2 = [
     "⣎⣵ ⣰⡀ ⢀⡀ ⡇   ⢺  ⣎⣵ ⠄ ⢀⡀",
     "⠫⠜ ⠘⠤ ⠣⠜ ⠣   ⠼⠄ ⠫⠜ ⠇ ⣑⡺"
    ]
    cim = [
" ____     ___  __ __    ___  _____  _____   ___   ____       _____ _____  ____  ____   ______ ",
"|    \   /  _]|  |  |  /  _]|     |/ ___/  /  _] /    |     / ___/|     ||    ||    \ |      |",
"|  _  | /  [_ |  |  | /  [_ |__/  (   \_  /  [_ |   __|    (   \_ |__/  | |  | |  _  ||      |",
"|  |  ||    _]|  _  ||    _]|   __|\__  ||    _]|  |  |     \__  ||   __| |  | |  |  ||_|  |_|",
"|  |  ||   [_ |  |  ||   [_ |  /  |/  \ ||   [_ |  |_ |     /  \ ||  /  | |  | |  |  |  |  |  ",
"|  |  ||     ||  |  ||     ||     |\    ||     ||     |     \    ||     | |  | |  |  |  |  |  ",
"|__|__||_____||__|__||_____||_____| \___||_____||___,_|      \___||_____||____||__|__|  |__|  "
                                                                                              
    ]
    while True:      
        asciiras(cim,"white")
        print("\n" * 4)
        asciiras(utasitas,"blue")
        asciiras(utasitas2,"blue")
        nehezsegiszint = input("")
        if(nehezsegiszint.isdigit()):
            nehezsegiszint = int(nehezsegiszint)
            if((nehezsegiszint<11 and nehezsegiszint>-1)):
                break
        cls()
def hardcore1():
    cls()
    global hardcore
    cim = [
" __ __   ____  ____   ___      __   ___   ____     ___ ",
"|  |  | /    ||    \ |   \    /  ] /   \ |    \   /  _]",
"|  |  ||  o  ||  D  )|    \  /  / |     ||  D  ) /  [_ ",
"|  _  ||     ||    / |  D  |/  /  |  O  ||    / |    _]",
"|  |  ||  _  ||    \ |     /   \_ |     ||    \ |   [_ ",
"|  |  ||  |  ||  .  \|     \     ||     ||  .  \|     |",
"|__|__||__|__||__|\_||_____|\____| \___/ |__|\_||_____|"
    ]
    kerdes = [
     "⣇⣸ ⢀⣀ ⡀⣀ ⢀⣸ ⢀⣀ ⢀⡀ ⡀⣀ ⢀⡀   ⣀⣀  ⢀⡀ ⢀⣸ ⣇⡀ ⢀⣀   ⢀⣀ ⣀⣀ ⢀⡀ ⡀⣀ ⢀⡀ ⣰⡀ ⣀⡀ ⢀⡀   ⡇ ⢀⡀ ⣀⡀ ⣀⡀ ⠄",
    " ⠇⠸ ⠣⠼ ⠏  ⠣⠼ ⠣⠤ ⠣⠜ ⠏  ⠣⠭   ⠇⠇⠇ ⠣⠜ ⠣⠼ ⠧⠜ ⠣⠼   ⠭⠕ ⠴⠥ ⠣⠭ ⠏  ⠣⠭ ⠘⠤ ⠇⠸ ⠣⠭   ⠣ ⠣⠭ ⡧⠜ ⠇⠸ ⠇"
    ]
    
    igen = r"""
     ⡇ ⢀⡀ ⢀⡀ ⣀⡀
     ⠇ ⣑⡺ ⠣⠭ ⠇⠸
    """
    nem = r"""
     ⡷⣸ ⢀⡀ ⣀⣀ 
     ⠇⠹ ⠣⠭ ⠇⠇⠇
    """
    options = [
    center_option(igen),
    center_option(nem)
    ]
    asciiras(cim,"white")
    asciiras(kerdes,"blue")
    Choice = inquirer.select(
        message = "",
        pointer = "",
        choices = options,
        multiselect = False,
        style = theme
    ).execute()
    if Choice == options[0]:
        hardcore = True
    else: 
        hardcore = False 
    

def nev(vilagnev):
    cls()
    cim = [
        " __  _    ___  _____  ___      ___  _____ ",
        "|  |/ ]  /  _]|     ||   \    /  _]/ ___/ ",
        "|  ' /  /  [_ |__/  ||    \  /  [_(   \_  ",
        "|    \ |    _]|   __||  D  ||    _]\__  | ",
        "|     ||   [_ |  /  ||     ||   [_ /  \ | ",
        "|  .  ||     ||     ||     ||     |\    | ",
        "|__|\_||_____||_____||_____||_____| \___| "
        ]
    instrukció = [
     "⣎⣱ ⢀⣸ ⠠ ⢀⣀   ⣀⣀  ⢀⡀ ⢀⡀   ⠠ ⢀⣀ ⣰⡀ ⢀⡀ ⡇⡠ ⣀⣀  ⢀⡀ ⣀⡀ ⢀⡀ ⣰⡀   ⣀⡀ ⢀⡀ ⡀⢀ ⢀⡀ ⣰⡀ ",
     "⠇⠸ ⠣⠼ ⡸ ⠣⠼   ⠇⠇⠇ ⠣⠭ ⣑⡺   ⡸ ⠣⠼ ⠘⠤ ⠣⠭ ⠏⠢ ⠇⠇⠇ ⠣⠭ ⠇⠸ ⠣⠭ ⠘⠤   ⠇⠸ ⠣⠭ ⠱⠃ ⠣⠭ ⠘⠤"
    ]
    
    asciiras(cim,"white")
    asciiras(instrukció,"blue")
    
    jateknev=input("")
    
    cls()
    cards.pakli.clear()
    cards.gyujt_stats.clear()
    cards.gyujtemeny.clear()
    for vilag in jatekmestermenu.vilagok:
        if vilag[0] == vilagnev:
            for kartya in vilag[2]:
                cards.add_to_collection(["",kartya])
    mentesek_fileread.mentesek.append([jateknev,[nehezsegiszint,hardcore].copy(),cards.gyujtemeny.copy(),cards.gyujt_stats.copy(),cards.pakli.copy(),vilagnev])
    mentes()
    mentesek_fileread.read_file("mentes.megprobaltuk")
    uj_gamemode.JATEK(jateknev)
    


def modosit(jateknev,vilagnev,beallitasok2):
    beallitasok = [0,False,False]
    beallitasok[0] = beallitasok2[0]
    if beallitasok2[1] == '1':
        beallitasok[1] = True
    else:
        beallitasok[1] = False  
    for i in range(len(mentesek_fileread.mentesek)):
        if mentesek_fileread.mentesek[i][0] == jateknev:
            mentesek_fileread.mentesek[i]=[jateknev,beallitasok.copy(),cards.gyujtemeny.copy(),cards.gyujt_stats.copy(),cards.pakli.copy(),vilagnev].copy()
            break
    mentes()





def mentes():

    cls()
    
    with open("mentes.megprobaltuk", "w", encoding = "utf-8") as file:
        for mentes in mentesek_fileread.mentesek: 
                # * beallitasok
                file.write(f"beallitasok;{mentes[1][0]};")
                if mentes[1][1]:
                    file.write("1;")
                else:
                    file.write("0;")
                if mentes[1][2]:
                    file.write("1\n")
                else:
                    file.write("0\n")
                # * vilagnev
                file.write(f"vilag;{mentes[5]}\n")
                # * gyujtemeny
                for kartya in mentes[2]:
                    file.write(f"felvetel gyujtemenybe;{kartya}\n")
                    file.write("\n")
                # * gyujt stats
                for stats in mentes[3]:
                    if stats is None:
                        print("HIBA: mentes[3] egy None statot tartalmaz!")
                        input("")
                        continue
                    file.write(f"stats;{stats["nev"]};{stats["sebzes"]};{stats["eletero"]};{stats["tipus"]}\n")
                file.write(f"uj pakli;")
                for i in range(0,(len(mentes[4]))):
                    if(i == len(mentes[4])-1):
                        file.write(f"{mentes[4][i]}")
                    else:
                        file.write(f"{mentes[4][i]},")
                file.write("\n")
                file.write(f"mentes;{mentes[0]}\n")
                file.write("\n")
                # * temp_kartyak
                # * temp_vezerek
                # * temp_kazamatak
                # * temp_gyujtemeny
                # * temp_vilagnev
    
