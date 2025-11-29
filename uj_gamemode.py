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
import mentesek_fileread
import os
import keyboard
import cards
import fileread
import kazamata
import time
from termcolor import colored, cprint
import kazamata
import fight
import new_kaz
import asciiart_converter
from InquirerPy.base.control import Choice
from InquirerPy.utils import color_print
from InquirerPy import get_style
from InquirerPy import inquirer
import new_cards
import math
import shutil
import random
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
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def cols():
    return os.get_terminal_size().columns

def rows():
    return os.get_terminal_size().lines

def asciiras(s,color):
    for line in s:
        cprint(line.center(cols()),f"{color}")
def center_option(text: str) -> str:
    return "\n".join(line.center(cols()) for line in text.split("\n"))

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
    mentesek_fileread.read_file("mentes.megprobaltuk")
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
        #time.sleep(0.5)
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

    


def JATEK(mentesnev):
    global jateknev 
    global vilagnev 
    global beallitasok 
    beallitasok = []
    jateknev = mentesnev
    for mentes in mentesek_fileread.mentesek:
        if mentes[0] == mentesnev: 
            for vilag in jatekmestermenu.vilagok:
                if vilag[0] == mentes[5]:
                    
                    vilagnev = vilag[0]
                    for kartya in vilag[1]:
                        if kartya["vezer"]:
                            new_cards.new_vezer(kartya)
                        else:
                            new_cards.new_card(kartya)
                    for kaz in vilag[3]:
                        new_kaz.new_kazamata(kaz)
            for kartya_nev in mentes[2]:
                cards.add_to_collection(["felvetel gyujtemenybe", kartya_nev])
            cards.pakli = mentes[4]
            beallitasok.append(mentes[1][0])
            beallitasok.append(mentes[1][1])
            beallitasok.append(mentes[1][2])

            
    menu2()
def menu2():
    cls()

    startt = r"""
     ⢎⡑ ⣰⡀ ⢀⣀ ⡀⣀ ⣰⡀
     ⠢⠜ ⠘⠤ ⠣⠼ ⠏  ⠘⠤
    """
    hasznalatiutasitast = r"""
    ⣇⣸ ⢀⣀ ⢀⣀ ⣀⣀ ⣀⡀ ⢀⣀ ⡇ ⢀⣀ ⣰⡀ ⠄   ⡀⢀ ⣰⡀ ⢀⣀ ⢀⣀ ⠄ ⣰⡀ ⢀⣀ ⢀⣀
    ⠇⠸ ⠣⠼ ⠭⠕ ⠴⠥ ⠇⠸ ⠣⠼ ⠣ ⠣⠼ ⠘⠤ ⠇   ⠣⠼ ⠘⠤ ⠣⠼ ⠭⠕ ⠇ ⠘⠤ ⠣⠼ ⠭⠕
    """
    vilagkartyaktext = r"""
     ⡇⢸ ⠄ ⡇ ⢀⣀ ⢀⡀ ⡇⡠ ⢀⣀ ⡀⣀ ⣰⡀ ⡀⢀ ⢀⣀ ⡇⡠
     ⠸⠃ ⠇ ⠣ ⠣⠼ ⣑⡺ ⠏⠢ ⠣⠼ ⠏  ⠘⠤ ⣑⡺ ⠣⠼ ⠏⠢
    """
    kazamatatext = r"""
     ⣇⠜ ⢀⣀ ⣀⣀ ⢀⣀ ⣀⣀  ⢀⣀ ⣰⡀ ⢀⣀ ⡇⡠
     ⠇⠱ ⠣⠼ ⠴⠥ ⠣⠼ ⠇⠇⠇ ⠣⠼ ⠘⠤ ⠣⠼ ⠏⠢
    """
    ujpaklitext = r"""
     ⡇⢸ ⠠   ⣀⡀ ⢀⣀ ⡇⡠ ⡇ ⠄
     ⠣⠜ ⡸   ⡧⠜ ⠣⠼ ⠏⠢ ⠣ ⠇
    """
    gyujtemenytext = r"""
     ⡎⠑ ⡀⢀ ⡀⢀ ⠠ ⣰⡀ ⢀⡀ ⣀⣀  ⢀⡀ ⣀⡀ ⡀⢀
     ⠣⠝ ⣑⡺ ⠣⠼ ⡸ ⠘⠤ ⠣⠭ ⠇⠇⠇ ⠣⠭ ⠇⠸ ⣑⡺
    """
    kileptext = r"""
     ⣇⠜ ⠄ ⡇ ⢀⡀ ⣀⡀ ⢀⡀ ⢀⣀
     ⠇⠱ ⠇ ⠣ ⠣⠭ ⡧⠜ ⠣⠭ ⠭⠕
    """

    centered_options = [
    center_option(startt),
    center_option(vilagkartyaktext),
    center_option(kazamatatext),
    center_option(ujpaklitext),
    center_option(gyujtemenytext),
    center_option(kileptext)
    ]
    choice = inquirer.select(
        message = "",
        pointer = "",
        choices = centered_options,
        multiselect = False,
        style = theme
        ).execute()
    if choice == centered_options[0]:
        kazamata_valaszto()
    if choice == centered_options[1]:
        vilagkartyak()
    if choice == centered_options[2]:
        kazamatafelsorolo()
    if choice == centered_options[3]:
        uj_pakli()
    if choice == centered_options[4]:
        gyujtemeny()
    if choice == centered_options[5]:
        os.system(f'taskkill /f /fi "WINDOWTITLE eq Damareen"')

        
    
    # ! vilagkartyak , kazamatak , uj pakli , gyujtemeny !!!!!!!!!!!!!!!!!!!!!!!!!!!!!ezeket csinald
    
# ! ##############################################################################################
def vilagkartyak():
    cls()
    printed = 0
    for i in range(0, len(cards.kartyak), 3):
        if len(cards.kartyak) - printed >= 3:
            print(" ________________        ________________        ________________".center(os.get_terminal_size().columns))
            print(f"|{cards.kartyak[i]["nev"].center(16)}|      |{cards.kartyak[i + 1]["nev"].center(16)}|      |{cards.kartyak[i + 2]["nev"].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(cards.kartyak[i]["sebzes"]) + "  E  " + str(cards.kartyak[i]["eletero"])).center(16)}|      |{("S  " + str(cards.kartyak[i + 1]["sebzes"]) + "  E  " + str(cards.kartyak[i + 1]["eletero"])).center(16)}|      |{("S  " + str(cards.kartyak[i + 2]["sebzes"]) + "  E  " + str(cards.kartyak[i + 2]["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.kartyak[i]["tipus"].center(16)}|      |{cards.kartyak[i + 1]["tipus"].center(16)}|      |{cards.kartyak[i + 2]["tipus"].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 3
        elif len(cards.gyujtemeny) - printed == 2:
            print(" ________________        ________________".center(os.get_terminal_size().columns))
            print(f"|{cards.kartyak[i]["nev"].center(16)}|      |{cards.kartyak[i+"nev"]["nev"].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(cards.kartyak[i]["sebzes"]) + "  E  " + str(cards.kartyak[i]["eletero"])).center(16)}|      |{("S  " + str(cards.kartyak[i + 1]["sebzes"]) + "  E  " + str(cards.kartyak[i + 1]["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.kartyak[i]["tipus"].center(16)}|      |{cards.kartyak[i + "nev"]["tipus"].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 2
        else:
            print(" ________________".center(os.get_terminal_size().columns))
            print(f"|{cards.kartyak[i]["nev"].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(cards.kartyak[i]["sebzes"]) + "  E  " + str(cards.kartyak[i]["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.kartyak[i]["tipus"].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 1


    printed = 0
    
    for i in range(0, len(cards.vezerek), 3):
            if len(cards.vezerek) - printed >= 3:
                cprint(" /\\/\\/\\/\\/\\/\\/\\/\\        /\\/\\/\\/\\/\\/\\/\\/\\        /\\/\\/\\/\\/\\/\\/\\/\\".center(os.get_terminal_size().columns), "yellow")
                cprint(f"|{cards.vezerek[i]["nev"].center(16)}|      |{cards.vezerek[i + 1]["nev"].center(16)}|      |{cards.vezerek[i + 2]["nev"].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(cards.vezerek[i]["sebzes"]) + "  E  " + str(cards.vezerek[i]["eletero"])).center(16)}|      |{("S  " + str(cards.vezerek[i + 1]["sebzes"]) + "  E  " + str(cards.vezerek[i + 1]["eletero"])).center(16)}|      |{("S  " + str(cards.vezerek[i + 2]["sebzes"]) + "  E  " + str(cards.vezerek[i + 2]["eletero"])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{cards.vezerek[i]["tipus"].center(16)}|      |{cards.vezerek[i + 1]["tipus"].center(16)}|      |{cards.vezerek[i + 2]["tipus"].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 3
            elif len(cards.vezerek) - printed == 2:
                
                cprint(" /\\/\\/\\/\\/\\/\\/\\/\\        /\\/\\/\\/\\/\\/\\/\\/\\".center(os.get_terminal_size().columns), "yellow")
                cprint(f"|{cards.vezerek[i]["nev"].center(16)}|      |{cards.vezerek[i+1]["nev"].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(cards.vezerek[i]["sebzes"]) + "  E  " + str(cards.vezerek[i]["eletero"])).center(16)}|      |{("S  " + str(cards.vezerek[i + 1]["sebzes"]) + "  E  " + str(cards.vezerek[i + 1]["eletero"])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{cards.vezerek[i]["tipus"].center(16)}|      |{cards.vezerek[i + 1]["tipus"].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns), "blue")
                printed += 2
            else:
                cprint(" /\\/\\/\\/\\/\\/\\/\\/\\".center(os.get_terminal_size().columns), "yellow")
                cprint(f"|{cards.vezerek[i]["nev"].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{("S  " + str(cards.vezerek[i]["sebzes"]) + "  E  " + str(cards.vezerek[i]["eletero"])).center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(f"|{cards.vezerek[i]["tipus"].center(16)}|".center(os.get_terminal_size().columns), "blue")
                cprint(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns),"blue")
                printed += 1





    print("")
    cprint("Nyomja meg az Enter-t a folytatashoz.".center(os.get_terminal_size().columns), "blue")
    input("")
    menu2()
# ! ################################################################################################
def kazamata_valaszto():
    cls()
    cim = [
 " _  __           ______         __  __       _______       _  __ ",
 "| |/ /    /\    |___  /   /\   |  \/  |   /\|__   __|/\   | |/ / ",
 "| ' /    /  \      / /   /  \  | \  / |  /  \  | |  /  \  | ' /  ",
 "|  <    / /\ \    / /   / /\ \ | |\/| | / /\ \ | | / /\ \ |  <   ",
 "| . \  / ____ \  / /__ / ____ \| |  | |/ ____ \| |/ ____ \| . \  ",
 "|_|\_\/_/    \_\/_____/_/    \_\_|  |_/_/    \_\_/_/    \_\_|\_\ "
                                                                 
                                                                 
    ]
    vilagok = kazamata.kazamatak
    opciok = [[]]
    for i in range(math.ceil(len(vilagok) / 3)):
        opciok.append([])
    for i in range(math.ceil(len(vilagok) / 3)):
        if len(vilagok) - (i * 3) <= 3:
            if i != 0:
                opciok[i].append(center_option(asciiart_converter.text_to_ascii("Elozo oldal", 1)))
                for j in range(i * 3, len(vilagok)):
                    opciok[i].append(center_option(asciiart_converter.text_to_ascii(vilagok[j]["nev"], 1)))
            else:
                for j in range(i * 3, len(vilagok)):
                    opciok[i].append(center_option(asciiart_converter.text_to_ascii(vilagok[j]["nev"], 1)))
        elif i == 0:
            for j in range(i * 3,(i * 3) + 3):
                opciok[i].append(center_option(asciiart_converter.text_to_ascii(vilagok[j]["nev"], 1)))
            opciok[i].append(center_option(asciiart_converter.text_to_ascii("Kovetkezo oldal", 1)))
        else:
            opciok[i].append(center_option(asciiart_converter.text_to_ascii("Elozo oldal", 1)))
            for j in range(i * 3,(i * 3) + 3):
                opciok[i].append(center_option(asciiart_converter.text_to_ascii(vilagok[j]["nev"], 1)))
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
# * kepessegek csak jatekosnak
# * tuz 3 kor utan + ceil ellenfel max 30% hp
# * fold 5 kor utan enemy kimarad + enemy 20% currenthp dmg
# * viz 2 kor utan 20% life steal
# * levego 2 kor 80% esely blockra
# * 10 kor one tap
    kaznev = asciiart_converter.ascii_to_text(choice)
    print(kaznev)
    input("")
    for kaz in kazamata.kazamatak:
        print(kaz["nev"])
        input("")
        if kaznev == kaz["nev"]:
            harc(kaz.copy())


    


# ! ################################################################################################
def uj_pakli():
    cls()
    printed = 0
    for i in range(0, len(cards.gyujt_stats), 3):
        if len(cards.gyujt_stats) - printed >= 3:
            print(" ________________        ________________        ________________".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["nev"].center(16)}|      |{cards.gyujt_stats[i + 1]["nev"].center(16)}|      |{cards.gyujt_stats[i + 2]["nev"].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(cards.gyujt_stats[i]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i]["eletero"])).center(16)}|      |{("S  " + str(cards.gyujt_stats[i + 1]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i + 1]["eletero"])).center(16)}|      |{("S  " + str(cards.gyujt_stats[i + 2]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i + 2]["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["tipus"].center(16)}|      |{cards.gyujt_stats[i + 1]["tipus"].center(16)}|      |{cards.gyujt_stats[i + 2]["tipus"].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 3
        elif len(cards.gyujtemeny) - printed == 2:
            print(" ________________        ________________".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["nev"].center(16)}|      |{cards.gyujt_stats[i+1]["nev"].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(cards.gyujt_stats[i]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i]["eletero"])).center(16)}|      |{("S  " + str(cards.gyujt_stats[i + 1]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i + 1]["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["tipus"].center(16)}|      |{cards.gyujt_stats[i + 1]["tipus"].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 2
        else:
            print(" ________________".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["nev"].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(cards.gyujt_stats[i]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i]["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["tipus"].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 1

    print("")
    
    
    cprint(f"Adja meg szokozokkel elvalasztva a kivalasztott kartyak nevet sorrendben, max. {round(len(cards.gyujt_stats) / 2)}".center(os.get_terminal_size().columns), "blue")
    while True:
        egyediek = set()
        if keyboard.is_pressed("esc"):
            menu2()
            break
        is_pakli_ready = True
        choice = input()
        valasztottak = choice.strip().split(" ")
        for valasztott in valasztottak:
            if len(valasztottak) > round(len(cards.gyujt_stats) / 2):
                cprint("Tul sokat adott meg!".center(os.get_terminal_size().columns), "red")
                is_pakli_ready = False
                break
            egyediek.add(valasztott)
            
            if cards.get_gyujt_stats(valasztott) == False:
                cprint("Adja meg a kartyakat helyesen!".center(os.get_terminal_size().columns), "red")
                is_pakli_ready = False
                break
            
        if (len(egyediek) < len(valasztottak)) and is_pakli_ready:
            cprint("Ne adjon meg tobb egyforma kartyat!".center(os.get_terminal_size().columns), "red")
            is_pakli_ready = False
        if is_pakli_ready:
            break
    cards.pakli = valasztottak
    jatekosmenu.modosit(jateknev,vilagnev,beallitasok)
    menu2()
    #harc(kiv_kaz)
# ! ################################################################################################
def gyujtemeny():
    cls()
    printed = 0
    for i in range(0, len(cards.gyujt_stats), 3):
        if len(cards.gyujt_stats) - printed >= 3:
            print(" ________________        ________________        ________________".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["nev"].center(16)}|      |{cards.gyujt_stats[i + 1]["nev"].center(16)}|      |{cards.gyujt_stats[i + 2]["nev"].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(cards.gyujt_stats[i]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i]["eletero"])).center(16)}|      |{("S  " + str(cards.gyujt_stats[i + 1]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i + 1]["eletero"])).center(16)}|      |{("S  " + str(cards.gyujt_stats[i + 2]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i + 2]["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["tipus"].center(16)}|      |{cards.gyujt_stats[i + 1]["tipus"].center(16)}|      |{cards.gyujt_stats[i + 2]["tipus"].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 3
        elif len(cards.gyujtemeny) - printed == 2:
            print(" ________________        ________________".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["nev"].center(16)}|      |{cards.gyujt_stats[i+1]["nev"].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(cards.gyujt_stats[i]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i]["eletero"])).center(16)}|      |{("S  " + str(cards.gyujt_stats[i + 1]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i + 1]["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["tipus"].center(16)}|      |{cards.gyujt_stats[i + 1]["tipus"].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 2
        else:
            print(" ________________".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["nev"].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(cards.gyujt_stats[i]["sebzes"]) + "  E  " + str(cards.gyujt_stats[i]["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujt_stats[i]["tipus"].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 1
    print("")
    cprint("Nyomja meg az Enter-t a folytatashoz.".center(os.get_terminal_size().columns), "blue")
    input("")
    menu2()


def kazamatafelsorolo():
    cls()
    cim = [
 " _  __           ______         __  __       _______       _  __ ",
 "| |/ /    /\    |___  /   /\   |  \/  |   /\|__   __|/\   | |/ / ",
 "| ' /    /  \      / /   /  \  | \  / |  /  \  | |  /  \  | ' /  ",
 "|  <    / /\ \    / /   / /\ \ | |\/| | / /\ \ | | / /\ \ |  <   ",
 "| . \  / ____ \  / /__ / ____ \| |  | |/ ____ \| |/ ____ \| . \  ",
 "|_|\_\/_/    \_\/_____/_/    \_\_|  |_/_/    \_\_/_/    \_\_|\_\ "
                                                                 
                                                                 
    ]
    asciiras(cim,"green")
    print("\n")

    for i in range(len(kazamata.kazamatak)):
        cprint(f"{kazamata.kazamatak[i]["nev"]}".center(os.get_terminal_size().columns), "blue")
        if kazamata.kazamatak[i]["tipus"] == "egyszeru":
            cprint("Egyszeru szintu kazamata".center(os.get_terminal_size().columns), "green")
        elif kazamata.kazamatak[i]["tipus"] == "kis": 
            cprint("Kis szintu kazamata".center(os.get_terminal_size().columns), "green")
        else:
            cprint("Nagy szintu kazamata".center(os.get_terminal_size().columns), "green")
        cprint("Tag(ok):".center(os.get_terminal_size().columns), "green")
        for j in range(len(kazamata.kazamatak[i]["kartyak"])):
            print(kazamata.kazamatak[i]["kartyak"][j].center(os.get_terminal_size().columns))
        if kazamata.kazamatak[i]["tipus"] == "egyszeru" or kazamata.kazamatak[i]["tipus"] == "kis":
            cprint(f"Jutalom: {kazamata.kazamatak[i]["fejlesztes"]}".center(os.get_terminal_size().columns), "green")
        else:
            cprint(f"Jutalom: kartya".center(os.get_terminal_size().columns), "green")
        print("")
    print("")
    cprint("Nyomja meg az Enter-t a folytatashoz.".center(os.get_terminal_size().columns), "blue")
    input()
    menu2()






harctext = [
" __ __   ____  ____      __  ",
"|  |  | /    ||    \    /  ] ",
"|  |  ||  o  ||  D  )  /  /  ",
"|  _  ||     ||    /  /  /   ",
"|  |  ||  _  ||    \ /   \_  ",
"|  |  ||  |  ||  .  \\     | ",
"|__|__||__|__||__|\_| \____| "
                            
]
def jatekostamad():
    # ODAMOZGÁS
    i = 41
    while i > 0:
        i -= 1
        lines = [
            f'{" " * (41 - i)}________________{" " * (i + 2)}________________'.center(os.get_terminal_size().columns),
            f'{" " * (40 - i)}|{jatekh["nev"].center(16)}|{" " * i}|{kazh["nev"].center(16)}|'.center(os.get_terminal_size().columns),
            f'{" " * (40 - i)}|{("S  "+str(jatekh["sebzes"])+"  E  "+str(jatekh["eletero"])).center(16)}|{" " * i}|{("S  "+str(kazh["sebzes"])+"  E  "+str(kazh["eletero"])).center(16)}|'.center(os.get_terminal_size().columns),
            f'{" " * (40 - i)}|{jatekh["tipus"].center(16)}|{" " * i}|{cards.stats(kazh["nev"])["tipus"].center(16)}|'.center(os.get_terminal_size().columns),
            f'{" " * (41 - i)}‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾{" " * (i + 2)}‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'.center(os.get_terminal_size().columns),
        ]
        print("\n".join(lines))
        time.sleep(0.05)
        cls()



    def random_hit_text(original):
        """16 karakter hosszú ütés-effekt: random csillagok."""
        result = []
        for ch in original:
            if ch != " " and random.random() < 0.35:
                result.append(YELLOW + "*" + RESET)
            else:
                result.append(ch)
        return "".join(result).ljust(16)[:16]

    for _ in range(4):

        # csillagos verzió generálása
        hit_name  = random_hit_text(kazh["nev"].center(16))
        hit_stats = random_hit_text(("S  "+str(kazh["sebzes"])+"  E  "+str(kazh["eletero"])).center(16))
        hit_type  = random_hit_text(cards.stats(kazh["nev"])["tipus"].center(16))

        # csillagos frame (találat)
        lines = [
            f'{" " * 40}________________  ________________'.center(os.get_terminal_size().columns),
            f'{" " * 39}|{jatekh["nev"].center(16)}| |{RED}{hit_name}{RESET}|'.center(os.get_terminal_size().columns),
            f'{" " * 39}|{("S  "+str(jatekh["sebzes"])+"  E  "+str(jatekh["eletero"])).center(16)}| |{RED}{hit_name}{RESET}|'.center(os.get_terminal_size().columns),
            f'{" " * 39}|{jatekh["tipus"].center(16)}| |{RED}{hit_name}{RESET}|'.center(os.get_terminal_size().columns),
            f'{" " * 40}‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'.center(os.get_terminal_size().columns),
        ]
        print("\n".join(lines))
        time.sleep(0.07)
        cls()

        # eredeti frame vissza
        lines = [
            f'{" " * 40}________________  ________________'.center(os.get_terminal_size().columns),
            f'{" " * 39}|{jatekh["nev"].center(16)}| |{kazh["nev"].center(16)}|'.center(os.get_terminal_size().columns),
            f'{" " * 39}|{("S  "+str(jatekh["sebzes"])+"  E  "+str(jatekh["eletero"])).center(16)}| |{("S  "+str(kazh["sebzes"])+"  E  "+str(kazh["eletero"])).center(16)}|'.center(os.get_terminal_size().columns),
            f'{" " * 39}|{jatekh["tipus"].center(16)}| |{cards.stats(kazh["nev"])["tipus"].center(16)}|'.center(os.get_terminal_size().columns),
            f'{" " * 40}‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'.center(os.get_terminal_size().columns),
        ]
        print("\n".join(lines))
        time.sleep(0.07)
        cls()

    # ---------------------------------------------------------
    #                VISSZAMOZGÁS
    # ---------------------------------------------------------
    i = 0
    while i < 41:
        i += 1
        lines = [
            f'{" " * (41 - i)}________________{" " * (i + 2)}________________'.center(os.get_terminal_size().columns),
            f'{" " * (40 - i)}|{jatekh["nev"].center(16)}|{" " * i}|{kazh["nev"].center(16)}|'.center(os.get_terminal_size().columns),
            f'{" " * (40 - i)}|{("S  "+str(jatekh["sebzes"])+"  E  "+str(jatekh["eletero"])).center(16)}|{" " * i}|{("S  "+str(kazh["sebzes"])+"  E  "+str(kazh["eletero"])).center(16)}|'.center(os.get_terminal_size().columns),
            f'{" " * (40 - i)}|{jatekh["tipus"].center(16)}|{" " * i}|{cards.stats(kazh["nev"])["tipus"].center(16)}|'.center(os.get_terminal_size().columns),
            f'{" " * (41 - i)}‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾{" " * (i + 2)}‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'.center(os.get_terminal_size().columns),
        ]

        print("\n".join(lines))
        time.sleep(0.05)
        cls()
def kazamatatamad(kazh, jatekh):
    cls()
    total_frames = 44
    max_shift = 40

    width = os.get_terminal_size().columns

    for frame in range(total_frames):
        cls()

        # oda-vissza mozgás
        if frame < total_frames // 2:
            shift = int(max_shift * (frame / (total_frames // 2)))
        else:
            shift = int(max_shift * (1 - (frame - total_frames // 2) / (total_frames // 2)))

        space = " " * shift

        L = [
            " ________________ ",
            f"|{jatekh['nev'].center(16)}|",
            f"|S {str(jatekh['sebzes']).center(3)} E {str(jatekh['eletero']).center(3)}|",
            f"|{jatekh['tipus'].center(16)}|",
            " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ "
        ]

        R = [
            " ________________ ",
            f"|{kazh['nev'].center(16)}|",
            f"|S {str(kazh['sebzes']).center(3)} E {str(kazh['eletero']).center(3)}      |",
            f"|{kazh['tipus'].center(16)}|",
            " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ "
        ]

        gap = " " * 40

        frame_lines = []
        for l, r in zip(L, R):
            line = f"{l}{gap}{space}{r}"
            frame_lines.append(line.center(width))
            
        print("\n".join(frame_lines))
        time.sleep(0.04)






def harc(kazamata):
    cls()
    global jatekh
    global kazh
    ellenfelek = kazamata["kartyak"]
    indexk = 0
    indexj = 0
    jatekh = cards.get_gyujt_stats(cards.pakli[indexj]).copy()
    kazh = cards.stats(ellenfelek[indexk]).copy()
    #while True:
        #if indexk >= len(ellenfelek):
        #    input()
        #    win_screen(kiv_kaz, True, indexj)
        #if indexj >= len(cards.pakli):
        #    input()
        #    win_screen(kiv_kaz, False, indexj)

    jatekostamad()
    input("")
       # print(" ________________        ________________".center(os.get_terminal_size().columns))
       # print(f"|{jatekh["nev"].center(16)}|      |{kazh["nev"].center(16)}|".center(os.get_terminal_size().columns))
       # print(f"|{("S  " + str(jatekh["sebzes"]) + "  E  " + str(jatekh["eletero"])).center(16)}|      |{("S  " + str(kazh["sebzes"]) + "  E  " + str(kazh["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
       # print(f"|{jatekh["tipus"].center(16)}|      |{cards.stats(kazh["nev"])["tipus"].center(16)}|".center(os.get_terminal_size().columns))
       # print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
# ! #################################################################################################################################################
    # ! MARADJ A FOR CIKLUSBAN
    """
        if kazh["eletero"] <= 0:
            kazh["eletero"] = 0
            indexk += 1
            if indexk >= len(ellenfelek):
                input()
                win_screen(kiv_kaz, True, indexj)
            if indexj >= len(cards.pakli):
                input()
                win_screen(kiv_kaz, False, indexj)
            print(f"A kazamata kijatszik egy kartyat: {ellenfelek[indexk]}")
            kazh = cards.stats(ellenfelek[indexk]).copy()
        else:
            if kazh["tipus"] != jatekh["tipus"]:
                    ktipus = fight.get_tipus_index(kazh["tipus"])
                    jtipus = fight.get_tipus_index(jatekh["tipus"])
                    if fight.tipusok[ktipus] == fight.tipusok[jtipus - 1] or fight.tipusok[ktipus] == fight.tipusok[jtipus + 1]:
                        jatekh["eletero"] -= kazh["sebzes"] * 2
                        print(f"A kazamata tamad: {kazh["sebzes"] * 2}")
                    else:
                        jatekh["eletero"] -= int(kazh["sebzes"] / 2)
                        print(f"A kazamata tamad: {int(kazh["sebzes"] / 2)}")
            else:
                jatekh["eletero"] -= kazh["sebzes"]
                print(f"A kazamata tamad: {kazh["sebzes"]}")
        if kazh["eletero"] <= 0:
            kazh["eletero"] = 0
        if jatekh["eletero"] <= 0:
            jatekh["eletero"] = 0

        
        input()
        cls()



        if jatekh["eletero"] <= 0:
            jatekh["eletero"] = 0
            indexj += 1
            if indexk >= len(ellenfelek):
                input()
                win_screen(kiv_kaz, True, indexj)
            if indexj >= len(cards.pakli):
                input()
                win_screen(kiv_kaz, False, indexj)
            print(f"A jatekos kijatszik egy kartyat: {cards.pakli[indexj]}")
            jatekh = cards.stats(cards.pakli[indexj]).copy()
        else:
            if jatekh["tipus"] != kazh["tipus"]:
                    ktipus = fight.get_tipus_index(jatekh["tipus"])
                    jtipus = fight.get_tipus_index(kazh["tipus"])
                    if fight.tipusok[ktipus] == fight.tipusok[jtipus - 1] or fight.tipusok[ktipus] == fight.tipusok[jtipus + 1]:
                        kazh["eletero"] -= jatekh["sebzes"] * 2
                        print(f"A jatekos tamad: {jatekh["sebzes"] * 2}")
                    else:
                        kazh["eletero"] -= int(jatekh["sebzes"] / 2)
                        print(f"A jatekos tamad: {int(jatekh["sebzes"] / 2)}")
            else:
                kazh["eletero"] -= jatekh["sebzes"]
                print(f"A jatekos tamad: {jatekh["sebzes"]}")
        if kazh["eletero"] <= 0:
            kazh["eletero"] = 0
        if jatekh["eletero"] <= 0:
            jatekh["eletero"] = 0
        """
        

fejlesztes = {
    "eletero": 2,
    "sebzes": 1,
}

# ! #################################################################################################################################################
def win_screen(kiv_kaz, nyert, indexj):
    cls()
    kstat=kazamata.kazamatak[kiv_kaz - 1]
    if nyert:
        cprint("A jatektosos nyert.", "green")
        if (kstat["tipus"] == "egyszeru" or kstat["tipus"] == "kis") : 
            
            for i in range(len(cards.gyujt_stats)):
                if cards.gyujt_stats[i]["nev"] == cards.pakli[indexj]:
                    cards.gyujt_stats[i][kstat["fejlesztes"]] += fejlesztes[kstat["fejlesztes"]]
                    print(f"\n A jutalmad:{cards.pakli[indexj]} kap + {kstat["fejlesztes"]}t")
                    break
        else:
            for kartya in kstat["kartyak"]:
                if(cards.get_gyujt_stats(kartya) == False):
                    cards.add_to_collection(cards.stats(kartya))
                    print(f"\n A jutalmad: ez a kartya {kartya} a gyüjteményedbe került")
                    break
    else:
        cprint("A jatekos vesztett.", "red")

    input()
    menu2()