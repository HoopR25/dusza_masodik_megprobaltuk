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

from time import sleep
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
    mentes = [
    "⣏⡉     ⡇⢸ ⠄ ⡇ ⢀⣀ ⢀⡀   ⡇ ⢀⡀ ⣀⣀  ⢀⡀ ⣀⡀ ⣰⡀ ⢀⡀ ⢀⣀ ⢀⡀ ",
    "⠤⠜ ⠶   ⠸⠃ ⠇ ⠣ ⠣⠼ ⣑⡺   ⠣ ⠣⠭ ⠇⠇⠇ ⠣⠭ ⠇⠸ ⠘⠤ ⠣⠭ ⠭⠕ ⠣⠭ "
    ]
    asciiras(gyujtemenytext,"red")
    print("\n"*3)
    asciiras(mentes,"red")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "1":
                clear_input_field()
                sleep(0.2)
                uj_kartya()
                break
            elif event.name == "2":
                clear_input_field()
                sleep(0.2)
                uj_vezerkartya()
                break
            elif event.name == "3":
                clear_input_field()
                sleep(0.2)
                uj_kazamata()
                break
            elif event.name == "4":
                clear_input_field()
                sleep(0.2)
                uj_gyujtemeny()
                break
            elif event.name == "5":
                clear_input_field()
                sleep(0.2)
                mentes()
                break
            elif event.name == "esc":
                sleep(0.2)
                jatekmestermenu()
                break

tipusok = ["fold", "levego", "viz", "tuz", "fold", "levego"]

temp_kartyak = []

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

    hiba = [
         "⣎⣱ ⢀⣸ ⠠ ⢀⣀   ⣀⣀  ⢀⡀ ⢀⡀   ⣇⡀ ⢀⡀ ⡇ ⡀⢀ ⢀⡀ ⢀⣀ ⢀⡀ ⣀⡀",
         "⠇⠸ ⠣⠼ ⡸ ⠣⠼   ⠇⠇⠇ ⠣⠭ ⣑⡺   ⠇⠸ ⠣⠭ ⠣ ⣑⡺ ⠣⠭ ⠭⠕ ⠣⠭ ⠇⠸"
    ]

    print("\n" * 3)
    asciiras(cim,"white")
    print("\n" * int(rows()/5))
    asciiras(hasznalat, "red")
    asciiras(hasznalat2, "red")
    print("")
    asciiras(parancs, "blue")
    print("\n" * 3)

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "esc":
                clear_input_field()
                vilagfelvetel()
                break
        clear_input_field()
        bemenet = input("")
        adatok = bemenet.strip().split(" ")
        if len(adatok) == 4 and len(adatok[0]) < 17 and adatok[1].isnumeric() and adatok[2].isnumeric() and van_benne(adatok[3]) and not van_temp_kartya(adatok[0]):
            clear_input_field()
            # TODO: mentes
            adatok.append(False)
            adatok2 = [False, adatok[0], int(adatok[1]), int(adatok[2]), adatok[3]] 
            temp_kartyak.append(adatok2)
            vilagfelvetel()
            break
        cls()
        print("\n" * 3)
        asciiras(cim,"white")
        print("\n" * int(rows()/5))
        asciiras(hiba, "red")
        asciiras(parancs, "blue")
        print("\n" * 3)
        sleep(0.2)
        


temp_vezerek = []

def uj_vezerkartya():
    
    cim = [
    " _    _ _                          ",
    "| |  | (_)                         ",
    "| |  | |_  __   _____ _______ _ __ ",
    "| |  | | | \ \ / / _ \_  / _ \ '__|",
    "| |__| | |  \ V /  __// /  __/ |   ",
    " \____/| |   \_/ \___/___\___|_|    ",
    "      _/ |                         ",
    "     |__/                          "
    ]
    nincs = [
    "⡷⣸ ⠄ ⣀⡀ ⢀⣀ ⢀⣀   ⡇ ⢀⡀ ⣰⡀ ⡀⣀ ⢀⡀ ⣇⡀ ⢀⡀ ⣀⣀ ⢀⡀ ⣰⡀ ⣰⡀   ⡇⡠ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀",
    "⠇⠹ ⠇ ⠇⠸ ⠣⠤ ⠭⠕   ⠣ ⠣⠭ ⠘⠤ ⠏  ⠣⠭ ⠇⠸ ⠣⠜ ⠴⠥ ⠣⠜ ⠘⠤ ⠘⠤   ⠏⠢ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼ "
    ]
    
    hasznalat = [
         "⣎⣱ ⢀⣸ ⠠ ⢀⣀   ⣀⣀  ⢀⡀ ⢀⡀   ⢀⣀ ⣀⣀   ⢀⣀ ⢀⣸ ⢀⣀ ⣰⡀ ⢀⡀ ⡇⡠ ⢀⣀ ⣰⡀",
         "⠇⠸ ⠣⠼ ⡸ ⠣⠼   ⠇⠇⠇ ⠣⠭ ⣑⡺   ⠣⠼ ⠴⠥   ⠣⠼ ⠣⠼ ⠣⠼ ⠘⠤ ⠣⠜ ⠏⠢ ⠣⠼ ⠘⠤"
    ]

    utasitas = [
    "⡀⢀ ⢀⡀ ⣀⣀ ⢀⡀ ⡀⣀ ⣀⡀ ⢀⡀ ⡀⢀   ⢀⣀ ⣀⣀ ⢀⣀ ⡀⣀ ⣀⣀  ⢀⣀ ⣀⣀ ⣰⡀ ⢀⣀ ⣰⡀ ⢀⣀ ⢀⣀   ⢀⣸ ⡀⢀ ⣀⡀ ⡇ ⢀⣀ ⣀⣀ ⢀⡀ ⢀⣀ ⣰⡀ ⢀⣀ ⣰⡀",
     "⠱⠃ ⠣⠭ ⠴⠥ ⠣⠭ ⠏  ⠇⠸ ⠣⠭ ⠱⠃   ⠭⠕ ⠴⠥ ⠣⠼ ⠏  ⠇⠇⠇ ⠣⠼ ⠴⠥ ⠘⠤ ⠣⠼ ⠘⠤ ⠣⠼ ⠭⠕   ⠣⠼ ⠣⠼ ⡧⠜ ⠣ ⠣⠼ ⠴⠥ ⠣⠜ ⠭⠕ ⠘⠤ ⠣⠼ ⠘⠤"
    ]
    kartyaktext = [
    "⣇⠜ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀ ⡇⡠",
    "⠇⠱ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼ ⠏⠢"
    ]

    hiba = [
         "⣎⣱ ⢀⣸ ⠠ ⢀⣀   ⣀⣀  ⢀⡀ ⢀⡀   ⣇⡀ ⢀⡀ ⡇ ⡀⢀ ⢀⡀ ⢀⣀ ⢀⡀ ⣀⡀",
         "⠇⠸ ⠣⠼ ⡸ ⠣⠼   ⠇⠇⠇ ⠣⠭ ⣑⡺   ⠇⠸ ⠣⠭ ⠣ ⣑⡺ ⠣⠭ ⠭⠕ ⠣⠭ ⠇⠸"
    ]




    cls()
    print("\n" * 3)
    asciiras(cim, "white")
    print("\n" * int(rows()/5))
    if len(temp_kartyak) == 0:
        asciiras(nincs, "red")
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "esc":
                    clear_input_field()
                    vilagfelvetel()
                    break
    else:
        asciiras(hasznalat, "blue")
        print("")
        asciiras(utasitas, "blue")
        print("\n\n")
        while True:
            asciiras(kartyaktext, "blue")       
            print("\n"*3)
            printed = 0
            for i in range(0, len(temp_kartyak), 3):
                if len(temp_kartyak) - printed >= 3:
                    cprint(" ________________        ________________        ________________".center(os.get_terminal_size().columns), "blue")
                    cprint(f"|{temp_kartyak[i][1].center(16)}|      |{temp_kartyak[i + 1][1].center(16)}|      |{temp_kartyak[i + 2][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                    cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 1][2]) + "  E  " + str(temp_kartyak[i + 1][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 2][2]) + "  E  " + str(temp_kartyak[i + 2][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                    cprint(f"|{temp_kartyak[i][4].center(16)}|      |{temp_kartyak[i + 1][4].center(16)}|      |{temp_kartyak[i + 2][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                    cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                    printed += 3
                elif len(temp_kartyak) - printed == 2:
                    cprint(" ________________        ________________".center(os.get_terminal_size().columns), "blue")
                    cprint(f"|{temp_kartyak[i][1].center(16)}|      |{temp_kartyak[i+1][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                    cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 1][2]) + "  E  " + str(temp_kartyak[i + 1][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                    cprint(f"|{temp_kartyak[i][4].center(16)}|      |{temp_kartyak[i + 1][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                    cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                    printed += 2
                else:
                    cprint(" ________________".center(os.get_terminal_size().columns), "blue")
                    cprint(f"|{temp_kartyak[i][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                    cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                    cprint(f"|{temp_kartyak[i][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                    cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns),"" "blue")
                    printed += 1
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "esc":
                    clear_input_field()
                    vilagfelvetel()
                    break
            clear_input_field()
            bemenet = input("")
            adatok = bemenet.strip().split()
            if len(adatok) == 3 and len(adatok[0]) < 17 and van_temp_kartya(adatok[1]) and van_jutalom(adatok[2]) and not van_temp_kartya(adatok[0]):
                clear_input_field()
                adatok.append(False)
                if adatok[2] == "sebzes":
                    adatok2 = [True, adatok[0], temp_stats(adatok[1])[2] * 2, temp_stats(adatok[1])[3], temp_stats(adatok[1])[4]] 
                elif adatok[2] == "eletero":
                    adatok2 = [True, adatok[0], temp_stats(adatok[1])[2], temp_stats(adatok[1])[3] * 2, temp_stats(adatok[1])[4]] 
                temp_vezerek.append(adatok2)
                vilagfelvetel()
                break
            cls()
            print("\n" * 3)
            asciiras(cim,"white")
            print("\n" * int(rows()/5))
            asciiras(hiba, "red")
            asciiras(utasitas, "red")
            print("\n" * 3)
            sleep(0.2)
        


def van_temp_kartya(nev):
    for kartya in temp_kartyak:
        if kartya[1] == nev:
            return True
    for kartya in temp_vezerek:
        if kartya[1] == nev:
            return True
    return False
        
temp_kazamatak = []

def uj_kazamata():
    cls()
    cim = [
 " _    _ _   _                                  _        ",
 "| |  | (_) | |                                | |       ",
 "| |  | |_  | | ____ _ ______ _ _ __ ___   __ _| |_ __ _ ",
 "| |  | | | | |/ / _` |_  / _` | '_ ` _ \ / _` | __/ _` |",
 "| |__| | | |   < (_| |/ / (_| | | | | | | (_| | || (_| |",
 " \____/| | |_|\_\__,_/___\__,_|_| |_| |_|\__,_|\__\__,_|",
 "      _/ |                                              ",
 "     |__/                                               "
    ]
    utasitas = [
     "⡇⢸ ⢀⣀ ⡇ ⢀⣀ ⢀⣀ ⢀⣀ ⣀⣀   ⣰⡀ ⠄ ⣀⡀ ⡀⢀ ⢀⣀ ⣰⡀",
     "⠸⠃ ⠣⠼ ⠣ ⠣⠼ ⠭⠕ ⠭⠕ ⠴⠥   ⠘⠤ ⠇ ⡧⠜ ⠣⠼ ⠭⠕ ⠘⠤"
    ]
    egyszerutext = [
      "⢺      ⣏⡉ ⢀⡀ ⡀⢀ ⢀⣀ ⣀⣀ ⢀⡀ ⡀⣀ ⡀⢀",
      "⠼⠄ ⠶   ⠧⠤ ⣑⡺ ⣑⡺ ⠭⠕ ⠴⠥ ⠣⠭ ⠏  ⠣⠼"
    ]
    kistext = [
      "⠊⡱     ⣇⠜ ⠄ ⢀⣀",
      "⠮⠤ ⠶   ⠇⠱ ⠇ ⠭⠕"
    ]
    nagytext = [
      " ⢉⡹     ⡷⣸ ⢀⣀ ⢀⡀ ⡀⢀",
      " ⠤⠜ ⠶   ⠇⠹ ⠣⠼ ⣑⡺ ⣑⡺"
    ]
    print("\n" * 3)
    asciiras(cim,"white")
    print("\n" * (int(rows()/5)))
    asciiras(utasitas,"blue")
    print("\n" * 3)
    asciiras(egyszerutext,"red")
    print("\n" * 3)
    asciiras(kistext,"red")
    print("\n" * 3)
    asciiras(nagytext,"red")
    print("\n" * 3)
############################
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "1":
                clear_input_field()
                sleep(0.2)
                egyszeru()
                break
            elif event.name == "2":
                clear_input_field()
                sleep(0.2)
                kis()
                break
            elif event.name == "3":
                clear_input_field()
                sleep(0.2)
                nagy()
                break
            elif event.name == "esc":
                clear_input_field()
                sleep(0.2)
                vilagfelvetel()
                break
################################################





vezertext = [
 "⡇⢸ ⢀⡀ ⣀⣀ ⢀⡀ ⡀⣀ ⢀⡀ ⡇⡠",
 "⠸⠃ ⠣⠭ ⠴⠥ ⠣⠭ ⠏  ⠣⠭ ⠏⠢"
]

nincsvezertext = [
      "⡷⣸ ⠄ ⣀⡀ ⢀⣀ ⢀⣀   ⡇ ⢀⡀ ⣰⡀ ⡀⣀ ⢀⡀ ⢀⡀ ⣀⣀ ⢀⡀ ⣰⡀ ⣰⡀   ⡀⢀ ⢀⡀ ⣀⣀ ⢀⡀ ⡀⣀",
      "⠇⠹ ⠇ ⠇⠸ ⠣⠤ ⠭⠕   ⠣ ⠣⠭ ⠘⠤ ⠏  ⠣⠭ ⠣⠜ ⠴⠥ ⠣⠜ ⠘⠤ ⠘⠤   ⠱⠃ ⠣⠭ ⠴⠥ ⠣⠭ ⠏ "
]

nincselegtext = [
     "⡷⣸ ⠄ ⣀⡀ ⢀⣀ ⢀⣀   ⢀⡀ ⡇ ⢀⡀ ⢀⡀   ⡇⡠ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀",
     "⠇⠹ ⠇ ⠇⠸ ⠣⠤ ⠭⠕   ⠣⠭ ⠣ ⠣⠭ ⣑⡺   ⠏⠢ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼"
]

def egyszeru():
    cls()
    utasitas = [
      "⡇⡠ ⢀⣀ ⣀⣀ ⢀⣀ ⣀⣀  ⢀⣀ ⣰⡀ ⢀⣀ ⣀⡀ ⢀⡀ ⡀⢀   ⡇⡠ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀ ⣀⡀ ⢀⡀ ⡀⢀   ⠠ ⡀⢀ ⣰⡀ ⢀⣀ ⡇ ⢀⡀ ⣀⣀ ",
      "⠏⠢ ⠣⠼ ⠴⠥ ⠣⠼ ⠇⠇⠇ ⠣⠼ ⠘⠤ ⠣⠼ ⠇⠸ ⠣⠭ ⠱⠃   ⠏⠢ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼ ⠇⠸ ⠣⠭ ⠱⠃   ⡸ ⠣⠼ ⠘⠤ ⠣⠼ ⠣ ⠣⠜ ⠇⠇⠇"
    ]
    kartyaktext = [
    "⣇⠜ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀ ⡇⡠",
    "⠇⠱ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼ ⠏⠢"
    ]
    cim = [
        " _    _ _                                     _                                  _        ",
        "| |  | (_)                                   | |                                | |       ",
        "| |  | |_    ___  __ _ ___ _______ _ __ _   _| | ____ _ ______ _ _ __ ___   __ _| |_ __ _ ",
        "| |  | | |  / _ \/ _` / __|_  / _ \ '__| | | | |/ / _` |_  / _` | '_ ` _ \ / _` | __/ _` |",
        "| |__| | | |  __/ (_| \__ \/ /  __/ |  | |_| |   < (_| |/ / (_| | | | | | | (_| | || (_| |",
        " \____/| |  \___|\__, |___/___\___|_|   \__,_|_|\_\__,_/___\__,_|_| |_| |_|\__,_|\__\__,_|",
        "      _/ |        __/ |                                                                   ",
        "     |__/        |___/                                                                    "
    ] 
    hiba = [
         "⣎⣱ ⢀⣸ ⠠ ⢀⣀   ⣀⣀  ⢀⡀ ⢀⡀   ⣇⡀ ⢀⡀ ⡇ ⡀⢀ ⢀⡀ ⢀⣀ ⢀⡀ ⣀⡀",
         "⠇⠸ ⠣⠼ ⡸ ⠣⠼   ⠇⠇⠇ ⠣⠭ ⣑⡺   ⠇⠸ ⠣⠭ ⠣ ⣑⡺ ⠣⠭ ⠭⠕ ⠣⠭ ⠇⠸"
    ]
    print("\n" * 3)
    asciiras(cim,"white")
    print("\n" *int(rows()/5)) 
    if len(temp_kartyak) < 1:
        asciiras(nincselegtext,"red")
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "esc":
                    clear_input_field()
                    uj_kazamata()
                    break
    print("\n" * 4)
    asciiras(utasitas,"blue")
    print("\n" * 4)
    while True:
        print("\n"*3)
        printed = 0
        asciiras(kartyaktext, "blue")      
        for i in range(0, len(temp_kartyak), 3):
            if len(temp_kartyak) - printed >= 3:
                cprint(" ________________        ________________        ________________".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][1].center(16)}|      |{temp_kartyak[i + 1][1].center(16)}|      |{temp_kartyak[i + 2][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 1][2]) + "  E  " + str(temp_kartyak[i + 1][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 2][2]) + "  E  " + str(temp_kartyak[i + 2][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][4].center(16)}|      |{temp_kartyak[i + 1][4].center(16)}|      |{temp_kartyak[i + 2][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 3
            elif len(temp_kartyak) - printed == 2:
                
                cprint(" ________________        ________________".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][1].center(16)}|      |{temp_kartyak[i+1][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 1][2]) + "  E  " + str(temp_kartyak[i + 1][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][4].center(16)}|      |{temp_kartyak[i + 1][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 2
            else:
                cprint(" ________________".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns),"" "blue")
                printed += 1
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "esc":
                clear_input_field()
                uj_kazamata()
                break
        clear_input_field()
        bemenet = input("")
        adatok = bemenet.strip().split(" ")
        if len(adatok) == 3 and len(adatok[0]) < 17 and van_sima(adatok[1]) and van_jutalom(adatok[2]) and not van_kaz(adatok[0]):
            temp_kazamatak.append(["placeholder", "egyszeru", adatok[0], [adatok[1]], adatok[2]])
            uj_kazamata()
            break
        cls()
        print("\n" * 3)
        asciiras(cim,"white")
        print("\n" * int(rows()/5))
        asciiras(hiba, "red")
        asciiras(utasitas, "red")
        print("\n" * 3)
        sleep(0.2)


def ugyanolyan(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j:
                if lista[i] == lista[j]:
                    return False
    return True


def kis():
    cls()
    utasitas = [
    "⡇⡠ ⢀⣀ ⣀⣀ ⢀⣀ ⣀⣀  ⢀⣀ ⣰⡀ ⢀⣀ ⣀⡀ ⢀⡀ ⡀⢀   ⢉⡹ ⡇⡠ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀ ⣀⡀ ⢀⡀ ⡀⢀   ⡀⢀ ⢀⡀ ⣀⣀ ⢀⡀ ⡀⣀ ⣀⡀ ⢀⡀ ⡀⢀   ⠠ ⡀⢀ ⣰⡀ ⢀⣀ ⡇ ⢀⡀ ⣀⣀ ",
    "⠏⠢ ⠣⠼ ⠴⠥ ⠣⠼ ⠇⠇⠇ ⠣⠼ ⠘⠤ ⠣⠼ ⠇⠸ ⠣⠭ ⠱⠃   ⠤⠜ ⠏⠢ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼ ⠇⠸ ⠣⠭ ⠱⠃   ⠱⠃ ⠣⠭ ⠴⠥ ⠣⠭ ⠏  ⠇⠸ ⠣⠭ ⠱⠃   ⡸ ⠣⠼ ⠘⠤ ⠣⠼ ⠣ ⠣⠜ ⠇⠇⠇"
    ]
    cim = [
    " _    _ _   _    _     _                                  _        ",
    "| |  | (_) | |  (_)   | |                                | |       ",
    "| |  | |_  | | ___ ___| | ____ _ ______ _ _ __ ___   __ _| |_ __ _ ",
    "| |  | | | | |/ / / __| |/ / _` |_  / _` | '_ ` _ \ / _` | __/ _` |",
    "| |__| | | |   <| \__ \   < (_| |/ / (_| | | | | | | (_| | || (_| |",
    " \____/| | |_|\_\_|___/_|\_\__,_/___\__,_|_| |_| |_|\__,_|\__\__,_|",
    "      _/ |                                                         ",
    "     |__/                                                          "
    ]
    kartyaktext = [
    "⣇⠜ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀ ⡇⡠",
    "⠇⠱ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼ ⠏⠢"
    ]
    hiba = [
         "⣎⣱ ⢀⣸ ⠠ ⢀⣀   ⣀⣀  ⢀⡀ ⢀⡀   ⣇⡀ ⢀⡀ ⡇ ⡀⢀ ⢀⡀ ⢀⣀ ⢀⡀ ⣀⡀",
         "⠇⠸ ⠣⠼ ⡸ ⠣⠼   ⠇⠇⠇ ⠣⠭ ⣑⡺   ⠇⠸ ⠣⠭ ⠣ ⣑⡺ ⠣⠭ ⠭⠕ ⠣⠭ ⠇⠸"
    ]
    print("\n" * 3)
    asciiras(cim, "white")
    print("\n" * int(rows() / 5))   
    if len(temp_kartyak) < 3:
        asciiras(nincselegtext, "red")
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "esc":
                    clear_input_field()
                    uj_kazamata()
                    break
    elif len(temp_vezerek) < 1:
        asciiras(nincsvezertext, "red")
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "esc":
                    clear_input_field()
                    uj_kazamata()
                    break
    print("\n" * 4)
    asciiras(utasitas,"blue")
    print("\n" * 4)
    while True:
        print("\n" * 3)
        printed = 0
        asciiras(kartyaktext, "blue")   
        for i in range(0, len(temp_kartyak), 3):
            if len(temp_kartyak) - printed >= 3:
                cprint(" ________________        ________________        ________________".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][1].center(16)}|      |{temp_kartyak[i + 1][1].center(16)}|      |{temp_kartyak[i + 2][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 1][2]) + "  E  " + str(temp_kartyak[i + 1][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 2][2]) + "  E  " + str(temp_kartyak[i + 2][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][4].center(16)}|      |{temp_kartyak[i + 1][4].center(16)}|      |{temp_kartyak[i + 2][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 3
            elif len(temp_kartyak) - printed == 2:
                
                cprint(" ________________        ________________".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][1].center(16)}|      |{temp_kartyak[i+1][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 1][2]) + "  E  " + str(temp_kartyak[i + 1][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][4].center(16)}|      |{temp_kartyak[i + 1][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 2
            else:
                cprint(" ________________".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns),"" "blue")
                printed += 1

        # ! VEZEREK
        asciiras(vezertext, "blue")
        for i in range(0, len(temp_vezerek), 3):
            if len(temp_vezerek) - printed >= 3:
                cprint(" /\\/\\/\\/\\/\\/\\/\\/\\        /\\/\\/\\/\\/\\/\\/\\/\\        /\\/\\/\\/\\/\\/\\/\\/\\".center(os.get_terminal_size().columns), "yellow")
                cprint(f"|{temp_vezerek[i][1].center(16)}|      |{temp_vezerek[i + 1][1].center(16)}|      |{temp_vezerek[i + 2][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_vezerek[i][2]) + "  E  " + str(temp_vezerek[i][3])).center(16)}|      |{("S  " + str(temp_vezerek[i + 1][2]) + "  E  " + str(temp_vezerek[i + 1][3])).center(16)}|      |{("S  " + str(temp_vezerek[i + 2][2]) + "  E  " + str(temp_vezerek[i + 2][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_vezerek[i][4].center(16)}|      |{temp_vezerek[i + 1][4].center(16)}|      |{temp_vezerek[i + 2][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 3
            elif len(temp_vezerek) - printed == 2:
                
                cprint(" /\\/\\/\\/\\/\\/\\/\\/\\        /\\/\\/\\/\\/\\/\\/\\/\\".center(os.get_terminal_size().columns), "yellow")
                cprint(f"|{temp_vezerek[i][1].center(16)}|      |{temp_vezerek[i+1][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_vezerek[i][2]) + "  E  " + str(temp_vezerek[i][3])).center(16)}|      |{("S  " + str(temp_vezerek[i + 1][2]) + "  E  " + str(temp_vezerek[i + 1][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_vezerek[i][4].center(16)}|      |{temp_vezerek[i + 1][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 2
            else:
                cprint(" /\\/\\/\\/\\/\\/\\/\\/\\".center(os.get_terminal_size().columns), "yellow")
                cprint(f"|{temp_vezerek[i][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_vezerek[i][2]) + "  E  " + str(temp_vezerek[i][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_vezerek[i][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns),"" "blue")
                printed += 1
        
        
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "esc":
                clear_input_field()
                uj_kazamata()
                break
        clear_input_field()
        bemenet = input("")
        adatok = bemenet.strip().split(" ")
        if len(adatok) == 6 and len(adatok[0]) < 17 and van_sima(adatok[1]) and van_sima(adatok[2]) and van_sima(adatok[3]) and van_vezer(adatok[4]) and van_jutalom(adatok[5]) and ugyanolyan([adatok[1], adatok[2], adatok[3]]) and not van_kaz(adatok[0]):
            temp_kazamatak.append(["placeholder", "kis", adatok[0], [adatok[1], adatok[2], adatok[3], adatok[4]], adatok[5]])
            uj_kazamata()
            break
        cls()
        print("\n" * 3)
        asciiras(cim,"white")
        print("\n" * int(rows()/5))
        asciiras(hiba, "red")
        asciiras(utasitas, "red")
        print("\n" * 3)
        sleep(0.2)






def nagy():
    cls()
    utasitas = [
 "⡇⡠ ⢀⣀ ⣀⣀ ⢀⣀ ⣀⣀  ⢀⣀ ⣰⡀ ⢀⣀ ⣀⡀ ⢀⡀ ⡀⢀   ⣏⡉ ⡇⡠ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀ ⣀⡀ ⢀⡀ ⡀⢀   ⡀⢀ ⢀⡀ ⣀⣀ ⢀⡀ ⡀⣀ ⣀⡀ ⢀⡀ ⡀⢀",
 "⠏⠢ ⠣⠼ ⠴⠥ ⠣⠼ ⠇⠇⠇ ⠣⠼ ⠘⠤ ⠣⠼ ⠇⠸ ⠣⠭ ⠱⠃   ⠤⠜ ⠏⠢ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼ ⠇⠸ ⠣⠭ ⠱⠃   ⠱⠃ ⠣⠭ ⠴⠥ ⠣⠭ ⠏  ⠇⠸ ⠣⠭ ⠱⠃"
    ]
    cim = [
        " _    _ _                           _                                  _        ", 
        "| |  | (_)                         | |                                | |       ",
        "| |  | |_   _ __   __ _  __ _ _   _| | ____ _ ______ _ _ __ ___   __ _| |_ __ _ ",
        "| |  | | | | '_ \ / _` |/ _` | | | | |/ / _` |_  / _` | '_ ` _ \ / _` | __/ _` |",
        "| |__| | | | | | | (_| | (_| | |_| |   < (_| |/ / (_| | | | | | | (_| | || (_| |",
        " \____/| | |_| |_|\__,_|\__, |\__, |_|\_\__,_/___\__,_|_| |_| |_|\__,_|\__\__,_|",
        "      _/ |               __/ | __/ |                                            ",
        "     |__/               |___/ |___/                                             "
    ]
    hiba = [
         "⣎⣱ ⢀⣸ ⠠ ⢀⣀   ⣀⣀  ⢀⡀ ⢀⡀   ⣇⡀ ⢀⡀ ⡇ ⡀⢀ ⢀⡀ ⢀⣀ ⢀⡀ ⣀⡀",
         "⠇⠸ ⠣⠼ ⡸ ⠣⠼   ⠇⠇⠇ ⠣⠭ ⣑⡺   ⠇⠸ ⠣⠭ ⠣ ⣑⡺ ⠣⠭ ⠭⠕ ⠣⠭ ⠇⠸"
    ]
    kartyaktext = [
    "⣇⠜ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀ ⡇⡠",
    "⠇⠱ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼ ⠏⠢"
    ]
    print("\n" * 3)
    asciiras(cim,"white")
    print("\n" * int(rows()/5))
    if len(temp_kartyak) < 5:
        asciiras(nincselegtext, "red")
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "esc":
                    clear_input_field()
                    uj_kazamata()
                    break
    elif len(temp_vezerek) < 1:
        asciiras(nincsvezertext, "red")
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "esc":
                    clear_input_field()
                    uj_kazamata()
                    break
    print("\n" * 4)
    asciiras(utasitas,"blue")
    print("\n" * 4)
    while True:
        asciiras(kartyaktext,"blue")
        printed = 0
        for i in range(0, len(temp_kartyak), 3):
            if len(temp_kartyak) - printed >= 3:
                cprint(" ________________        ________________        ________________".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][1].center(16)}|      |{temp_kartyak[i + 1][1].center(16)}|      |{temp_kartyak[i + 2][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 1][2]) + "  E  " + str(temp_kartyak[i + 1][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 2][2]) + "  E  " + str(temp_kartyak[i + 2][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][4].center(16)}|      |{temp_kartyak[i + 1][4].center(16)}|      |{temp_kartyak[i + 2][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 3
            elif len(temp_kartyak) - printed == 2:
                    
                cprint(" ________________        ________________".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][1].center(16)}|      |{temp_kartyak[i+1][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|      |{("S  " + str(temp_kartyak[i + 1][2]) + "  E  " + str(temp_kartyak[i + 1][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][4].center(16)}|      |{temp_kartyak[i + 1][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 2
            else:
                cprint(" ________________".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_kartyak[i][2]) + "  E  " + str(temp_kartyak[i][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_kartyak[i][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns),"" "blue")
                printed += 1

        # ! VEZEREK
        asciiras(vezertext, "blue")
        for i in range(0, len(temp_vezerek), 3):
            if len(temp_vezerek) - printed >= 3:
                cprint(" /\\/\\/\\/\\/\\/\\/\\/\\        /\\/\\/\\/\\/\\/\\/\\/\\        /\\/\\/\\/\\/\\/\\/\\/\\".center(os.get_terminal_size().columns), "yellow")
                cprint(f"|{temp_vezerek[i][1].center(16)}|      |{temp_vezerek[i + 1][1].center(16)}|      |{temp_vezerek[i + 2][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_vezerek[i][2]) + "  E  " + str(temp_vezerek[i][3])).center(16)}|      |{("S  " + str(temp_vezerek[i + 1][2]) + "  E  " + str(temp_vezerek[i + 1][3])).center(16)}|      |{("S  " + str(temp_vezerek[i + 2][2]) + "  E  " + str(temp_vezerek[i + 2][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_vezerek[i][4].center(16)}|      |{temp_vezerek[i + 1][4].center(16)}|      |{temp_vezerek[i + 2][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 3
            elif len(temp_vezerek) - printed == 2:
                
                cprint(" /\\/\\/\\/\\/\\/\\/\\/\\        /\\/\\/\\/\\/\\/\\/\\/\\".center(os.get_terminal_size().columns), "yellow")
                cprint(f"|{temp_vezerek[i][1].center(16)}|      |{temp_vezerek[i+1][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_vezerek[i][2]) + "  E  " + str(temp_vezerek[i][3])).center(16)}|      |{("S  " + str(temp_vezerek[i + 1][2]) + "  E  " + str(temp_vezerek[i + 1][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_vezerek[i][4].center(16)}|      |{temp_vezerek[i + 1][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 2
            else:
                cprint(" /\\/\\/\\/\\/\\/\\/\\/\\".center(os.get_terminal_size().columns), "yellow")
                cprint(f"|{temp_vezerek[i][1].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(temp_vezerek[i][2]) + "  E  " + str(temp_vezerek[i][3])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{temp_vezerek[i][4].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns),"" "blue")
                printed += 1
            
            
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "esc":
                clear_input_field()
                uj_kazamata()
                break
        clear_input_field()
        bemenet = input("")
        adatok = bemenet.strip().split(" ")
        if len(adatok) == 7 and len(adatok[0]) < 17 and van_sima(adatok[1]) and van_sima(adatok[2]) and van_sima(adatok[3]) and van_sima(adatok[4]) and van_sima(adatok[5]) and van_vezer(adatok[6]) and ugyanolyan([adatok[1], adatok[2], adatok[3], adatok[4], adatok[5], adatok[6]]) and not van_kaz(adatok[0]):
            temp_kazamatak.append(["placeholder", "nagy", adatok[0], [adatok[1], adatok[2], adatok[3], adatok[4]], adatok[5]])
            uj_kazamata()
            break
        cls()
        print("\n" * 3)
        asciiras(cim,"white")
        print("\n" * int(rows()/5))
        asciiras(hiba, "red")
        asciiras(utasitas, "red")
        print("\n" * 3)
        sleep(0.2)






def uj_gyujtemeny():
    print("gyujtemeny")

def mentes():
    print("mentve")

def van_benne(arg):
    for tipus in tipusok:
        if tipus == arg:
            return True
    return False

def temp_stats(nev):
    for kartya in temp_kartyak:
        if kartya[1] == nev:
            return kartya.copy()

def van_jutalom(text):
    if text == "sebzes" or text == "eletero":
        return True
    else:
        return False
    
def van_kaz(nev):
    for kaz in temp_kazamatak:
        if kaz[2] == nev:
            return True
    return False


def van_vezer(nev):
    for vezer in temp_vezerek:
        if vezer[1] == nev:
            return True
    return False

def van_sima(nev):
    for kartya in temp_kartyak:
        if kartya[1] == nev:
            return True
    return False