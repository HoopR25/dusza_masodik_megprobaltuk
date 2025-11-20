import os
import keyboard
import cards
import fileread
import kazamata
import time
from termcolor import colored, cprint
import kazamata
import fight

import msvcrt

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def cols():
    return os.get_terminal_size().columns

def rows():
    return os.get_terminal_size().lines

def asciiras(s):
    for line in s:
        print(line.center(cols()))


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
    asciiras(tajekoztato)
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
                jatekmestermenu()
                break
            elif event.name == "2":
                jatekosmenu()
                break
            elif event.name == "3":
                leiras()
                break     
def leiras():
    print("")    

#péntek belekezdeni TODO:
def jatekmestermenu():
    print("uj vilag")
    
#szombat megcsinálni TODO:
def jatekosmenu():
    print("1. Uj vilag")
    print("2. Betoltes")
    print("3. Szabályzat")
    print("4. világok")
    
    

def vilagvalasto():                                                                                 
    print("vilagok felsorolva")


def jatekmode():
    print("nehezseg")
    print("DLC")
################################
#vasárnap TODO:
def meglevo():
    print("regi harc")