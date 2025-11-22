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

def betoltokepernyo():
    
    cls()
    ascii_art = [
    " _______                                                                            ",
    "/       \                                                                           ",
    "$$$$$$$  |  ______   _____  ____    ______    ______    ______    ______   _______  ",
    "$$ |  $$ | /      \ /     \/    \  /      \  /      \  /      \  /      \ /       \ ",
    "$$ |  $$ | $$$$$$  |$$$$$$ $$$$  | $$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$$  |",
    "$$ |  $$ | /    $$ |$$ | $$ | $$ | /    $$ |$$ |  $$/ $$    $$ |$$    $$ |$$ |  $$ |",
    "$$ |__$$ |/$$$$$$$ |$$ | $$ | $$ |/$$$$$$$ |$$ |      $$$$$$$$/ $$$$$$$$/ $$ |  $$ |",
    "$$    $$/ $$    $$ |$$ | $$ | $$ |$$    $$ |$$ |      $$       |$$       |$$ |  $$ |",
    "$$$$$$$/   $$$$$$$/ $$/  $$/  $$/  $$$$$$$/ $$/        $$$$$$$/  $$$$$$$/ $$/   $$/ "
    ]

    


    vpad = (rows() - len(ascii_art)) // 2

    print("\n" * (vpad - 4))  

    for line in ascii_art:
        time.sleep(0.5)
        cprint(line.center(cols()),"green")
    print("\n "*5)
    
    time.sleep(0.5)
    while True:
        cprint("Nyomd meg az entert a folytatashoz".center(cols()), "green") 
        start= time.time()
        bool = False
        while(time.time()-start<0.5):
            if(keyboard.is_pressed("\n")):
                bool=True
                clear_input_field()
                break
        if(bool):
            break
        print("\033[F", end="")
        print(" " * cols(), end="\r")
        start= time.time()
        while(time.time()-start<0.5):
            if(keyboard.is_pressed("\n")):
                bool=True
                clear_input_field()
                break
        if(bool):
            break
    input("")
    cls()
    menu()
    
def menu():
    cls()
    print("\n")
    jatekos =[
    "⠊⡱     ⠈⢹ ⢀⣀ ⣰⡀ ⢀⡀ ⡇⡠ ⢀⡀ ⢀⣀",
    "⠮⠤ ⠶   ⠣⠜ ⠣⠼ ⠘⠤ ⠣⠭ ⠏⠢ ⠣⠜ ⠭⠕"
    ]
    
    jatekmester =[
    " ⢺      ⠈⢹ ⢀⣀ ⣰⡀ ⢀⡀ ⡇⡠ ⣀⣀  ⢀⡀ ⢀⣀ ⣰⡀ ⢀⡀ ⡀⣀",
    " ⠼⠄ ⠶   ⠣⠜ ⠣⠼ ⠘⠤ ⠣⠭ ⠏⠢ ⠇⠇⠇ ⠣⠭ ⠭⠕ ⠘⠤ ⠣⠭ ⠏ "
    ]

    guide =[
        " ⢉⡹     ⡇  ⢀⡀ ⠄ ⡀⣀ ⢀⣀ ⢀⣀",
        " ⠤⠜ ⠶   ⠧⠤ ⠣⠭ ⠇ ⠏  ⠣⠼ ⠭⠕"
    ]
    tajekoztato=[
"__      __   _                                                             _       _      _                  _ ",
"\ \    / /  | |                                                           (_)     | |    | |                | |",
" \ \  / /_ _| | __ _ ___ ___ _______  _ __     __ _ ____   ___  _ __   ___ _  ___ | | __ | | _____ _____   _| | ",
"  \ \/ / _` | |/ _` / __/ __|_  / _ \| '_ \   / _` |_  /  / _ \| '_ \ / __| |/ _ \| |/ / | |/ / _ \_  / | | | | ",
"   \  / (_| | | (_| \__ \__ \/ / (_) | | | | | (_| |/ /  | (_) | |_) | (__| | (_) |   <  |   < (_) / /| |_| | | ",
"    \/ \__,_|_|\__,_|___/___/___\___/|_| |_|  \__,_/___|  \___/| .__/ \___|_|\___/|_|\_\ |_|\_\___/___|\__,_|_| ",
"                                                               | |                                              ",
"                                                               |_|                                              "    

         
    ]
    asciiras(tajekoztato,"white")
    print("\n"*3)
    cprint(jatekmester[0].center(cols()),"red")
    cprint(jatekmester[1].center(cols()),"red")
    print("\n"*3)
    cprint(jatekos[0].center(cols()),"red")
    cprint(jatekos[1].center(cols()),"red")
    cprint("\n"*3)
    cprint(guide[0].center(cols()),"blue")
    cprint(guide[1].center(cols()),"blue")
    # ! KEYBOARD BEOLVASAS
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "1":
                clear_input_field()
                jatekmestermenu()
                break
            elif event.name == "2":
                clear_input_field()
                jatekosmenu()
                break
            elif event.name == "3":
                clear_input_field()
                leiras()
                break
            elif event.name == "esc":
                sys.exit(1)
                os.system(f'taskkill /f /fi "WINDOWTITLE eq Damareen"')
def leiras():
        print()


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
                menu()
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

    
#szombat megcsinálni
def jatekosmenu():
    print("1. Uj vilag")
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


def uj_kartya():
    print("kartya")

def uj_vezerkartya():
    print("vezerkartya")

def uj_kazamata():
    print("kazamata")

def uj_gyujtemeny():
    print("gyujtemeny")