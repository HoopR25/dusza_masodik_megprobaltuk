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
import uj_gamemode
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
        
def jatekmestermenu():
    cls()
    print("\n" * 3)
    jatekmester = [

 " ____   ____  ______    ___  __  _  ___ ___    ___  _____ ______    ___  ____   ",
 "|    | /    ||      |  /  _]|  |/ ]|   |   |  /  _]/ ___/|      |  /  _]|    \  ",
 "|__  ||  o  ||      | /  [_ |  ' / | _   _ | /  [_(   \_ |      | /  [_ |  D  ) ",
 "__|  ||     ||_|  |_||    _]|    \ |  \_/  ||    _]\__  ||_|  |_||    _]|    /  ",
"/  |  ||  _  |  |  |  |   [_ |     \|   |   ||   [_ /  \ |  |  |  |   [_ |    \  ",
"\  `  ||  |  |  |  |  |     ||  .  ||   |   ||     |\    |  |  |  |     ||  .  \ ",
 "\____j|__|__|  |__|  |_____||__|\_||___|___||_____| \___|  |__|  |_____||__|\_| "
    ]
    
    asciiras(jatekmester,"white")
    ujvilag =[
    " ⢺      ⡀⢀ ⠠   ⡀⢀ ⠄ ⡇ ⢀⣀ ⢀⡀ ",
    " ⠼⠄ ⠶   ⠣⠼ ⡸   ⠱⠃ ⠇ ⠣ ⠣⠼ ⣑⡺"
    ]

    # TODO: Kilepes!

    print("\n" * (int(rows()/4)))
    asciiras(ujvilag,"red")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "1":
                vilagfelvetel()
                break
            elif event.name == "esc":
                uj_gamemode.menu()
                break




def vilagfelvetel():
    cls()
    
    ujvilag =[
" __ __  ____      __ __  ____  _       ____   ____ ",
"|  |  ||    |    |  |  ||    || |     /    | /    |",
"|  |  ||__  |    |  |  | |  | | |    |  o  ||   __|",
"|  |  |__|  |    |  |  | |  | | |___ |     ||  |  |",
"|  :  /  |  |    |  :  | |  | |     ||  _  ||  |_ |",
"|     \  `  |     \   /  |  | |     ||  |  ||     |",
" \__,_|\____|      \_/  |____||_____||__|__||___,_|"
    ]    
    asciiras(ujvilag,"white")
    print("\n" * (int(rows()/6)))
    kartyatext = [
     "⢺      ⡇⡠ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀",
     "⠼⠄ ⠶   ⠏⠢ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼"
    ] 
    asciiras(kartyatext,"red")
    print("\n" *3)
    
    vezerkartyatext = [
      "⠊⡱     ⡀⢀ ⢀⡀ ⣀⣀ ⢀⡀ ⡀⣀ ⡇⡠ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀",
      "⠮⠤ ⠶   ⠱⠃ ⠣⠭ ⠴⠥ ⠣⠭ ⠏  ⠏⠢ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼"
    ]
    asciiras(vezerkartyatext,"red")
    print("\n" *3)
    kazamatatext = [
     "⢉⡹     ⡇⡠ ⢀⣀ ⣀⣀ ⢀⣀ ⣀⣀  ⢀⣀ ⣰⡀ ⢀⣀",
     "⠤⠜ ⠶   ⠏⠢ ⠣⠼ ⠴⠥ ⠣⠼ ⠇⠇⠇ ⠣⠼ ⠘⠤ ⠣⠼"
    ]
    asciiras(kazamatatext,"red")
    print("\n" *3)
    gyujtemenytext = [
    "⢇⣸   ⢀⡀ ⡀⢀ ⡀⢀ ⠠ ⣰⡀ ⢀⡀ ⣀⣀  ⢀⡀ ⣀⡀ ⡀⢀",
    " ⠸ ⠶ ⣑⡺ ⣑⡺ ⠣⠼ ⡸ ⠘⠤ ⠣⠭ ⠇⠇⠇ ⠣⠭ ⠇⠸ ⣑⡺"
    ]
    asciiras(gyujtemenytext,"red")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "1":
                clear_input_field()

                uj_kartya()
                break
            elif event.name == "2":
                clear_input_field()
                
                uj_vezerkartya()
                break
            elif event.name == "3":
                clear_input_field()

                uj_kazamata()
                break
            elif event.name == "4":
                clear_input_field()
                
                uj_gyujtemeny()
                break
            elif event.name == "esc":
                jatekmestermenu()
                break



def uj_kartya():
    cls()
    cim = [
 " _    _ _   _              _               ",
 "| |  | (_) | |            | |              ",
 "| |  | |_  | | ____ _ _ __| |_ _   _  __ _ ",
 "| |  | | | | |/ / _` | '__| __| | | |/ _` |",
 "| |__| | | |   < (_| | |  | |_| |_| | (_| |",
 " \____/| | |_|\_\__,_|_|   \__|\__, |\__,_|",
 "      _/ |                      __/ |      ",
 "     |__/                      |___/       ",
    ]
    
    hasznalat = [
         "⣎⣱ ⢀⣸ ⠠ ⢀⣀   ⣀⣀  ⢀⡀ ⢀⡀   ⢀⣀ ⣀⣀   ⢀⣀ ⢀⣸ ⢀⣀ ⣰⡀ ⢀⡀ ⡇⡠ ⢀⣀ ⣰⡀",
         "⠇⠸ ⠣⠼ ⡸ ⠣⠼   ⠇⠇⠇ ⠣⠭ ⣑⡺   ⠣⠼ ⠴⠥   ⠣⠼ ⠣⠼ ⠣⠼ ⠘⠤ ⠣⠜ ⠏⠢ ⠣⠼ ⠘⠤"
    ]

    hasznalat2 = [
         "⢀⣀ ⣀⣀ ⢀⡀ ⡇⡠ ⢀⡀ ⣀⣀ ⣀⣀ ⢀⡀ ⡇   ⢀⡀ ⡇ ⡀⢀ ⢀⣀ ⡇ ⢀⣀ ⢀⣀ ⣀⣀ ⣰⡀ ⡀⢀ ⢀⣀",
         "⠭⠕ ⠴⠥ ⠣⠜ ⠏⠢ ⠣⠜ ⠴⠥ ⠴⠥ ⠣⠭ ⠣   ⠣⠭ ⠣ ⠱⠃ ⠣⠼ ⠣ ⠣⠼ ⠭⠕ ⠴⠥ ⠘⠤ ⠱⠃ ⠣⠼"
    ]

    parancs = [
         "⡇⡠ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀ ⣀⡀ ⢀⡀ ⡀⢀   ⢀⣀ ⢀⡀ ⣇⡀ ⣀⣀ ⢀⡀ ⢀⣀   ⢀⡀ ⡇ ⢀⡀ ⣰⡀ ⢀⡀ ⡀⣀ ⢀⡀   ⣰⡀ ⠄ ⣀⡀ ⡀⢀ ⢀⣀",
         " ⠏⠢ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼ ⠇⠸ ⠣⠭ ⠱⠃   ⠭⠕ ⠣⠭ ⠧⠜ ⠴⠥ ⠣⠭ ⠭⠕   ⠣⠭ ⠣ ⠣⠭ ⠘⠤ ⠣⠭ ⠏  ⠣⠜   ⠘⠤ ⠇ ⡧⠜ ⠣⠼ ⠭⠕ "
    ]

    print("\n" * 3)
    asciiras(cim,"white")
    print("\n" * int(rows()/5))
    asciiras(hasznalat, "red")
    #print("")
    asciiras(hasznalat2, "red")
    print("")
    asciiras(parancs, "blue")
    print("\n" * 3)
    clear_input_field()
    bemenet = input("")
    adatok = bemenet.split(" ")



def uj_vezerkartya():
    print("vezerkartya")

def uj_kazamata():
    print("kazamata")

def uj_gyujtemeny():
    print("gyujtemeny")
