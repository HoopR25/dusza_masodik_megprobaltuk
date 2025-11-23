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
import jatekosmenu
import jatekmestermenu
import new_fileread

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
    if os.path.getsize("jatekkornyezetek.megprobaltuk") == 0:
        with open("jatekkornyezetek.megprobaltuk", "w", encoding = "utf-8") as file:
                # ! ALAP VILAG MENTESE

                file.write("uj kartya;Arin;2;5;fold\n")
                file.write("uj kartya;Liora;2;4;levego\n")
                file.write("uj kartya;Nerun;3;3;tuz\n")
                file.write("uj kartya;Torak;3;4;fold\n")
                file.write("uj kartya;Selia;2;6;viz\n")
                file.write("uj kartya;Emera;2;5;levego\n")
                file.write("uj kartya;Vorn;2;7;viz\n")
                file.write("uj kartya;Kael;3;5;tuz\n")
                file.write("uj kartya;Myra;2;6;fold\n")
                file.write("uj kartya;Thalen;3;5;levego\n")
                file.write("uj kartya;Isara;2;6;viz\n")

                file.write("uj vezer;Lord Torak;Torak;sebzes\n")
                file.write("uj vezer;Priestess Selia;Selia;eletero\n\n")

                file.write("uj kazamata;egyszeru;Barlangi Portya;Nerun;sebzes\n")
                file.write("uj kazamata;kis;Osi Szentely;Arin,Emera,Selia,Lord Torak;eletero\n")
                file.write("uj kazamata;nagy; A melyseg kiralynoje;Liora,Arin,Selia,Nerun,Torak;Priestess Selia\n\n")

                file.write("felvetel gyujtemenybe;Arin\n")
                file.write("felvetel gyujtemenybe;Liora\n")
                file.write("felvetel gyujtemenybe;Selia\n")
                file.write("felvetel gyujtemenybe;Nerun\n")
                file.write("felvetel gyujtemenybe;Torak\n")
                file.write("felvetel gyujtemenybe;Emera\n")
                file.write("felvetel gyujtemenybe;Kael\n")
                file.write("felvetel gyujtemenybe;Myra\n")
                file.write("felvetel gyujtemenybe;Thalen\n")
                file.write("felvetel gyujtemenybe;Isara\n\n")

                file.write("uj vilag;alap\n")
                file.write("\n\n")
        new_fileread.read_file("jatekkornyezetek.megprobaltuk")
    else:
        new_fileread.read_file("jatekkornyezetek.megprobaltuk")
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
                jatekmestermenu.jatekmestermenu()
                break
            elif event.name == "2":
                clear_input_field()
                jatekosmenu.jatekosmenu()
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


