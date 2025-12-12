import os
import keyboard
import cards
import fileread
import kazamata
import time
from termcolor import colored, cprint
import kazamata
import fight

game_kartyak = [
    [False, "Arin", 2, 5, "fold"],
    [False, "Liora", 2, 4, "levego"],
    [False, "Nerun", 3, 3, "tuz"],
    [False, "Selia", 2, 6, "viz"],
    [False, "Torak", 3, 4, "fold"],
    [False, "Emera", 2, 5, "levego"],
    [False, "Vorn", 2, 7, "viz"],
    [False, "Kael", 3, 5, "tuz"],
    [False, "Myra", 2, 6, "fold"],
    [False, "Thalen", 3, 5, "levego"],
    [False, "Isara", 2, 6, "viz"],
    [True, "Lord Torak", 6, 4, "fold"],
    [True, "Priestess Selia", 2, 12, "viz"]
]

game_kazamatak = [
    ["kazamata", "egyszeru", "Barlangi Portya", "Nerun", "sebzes"],
    ["kazamata", "kis", "Osi Szentely", "Arin", "Emera", "Selia", "Lord Torak", "eletero"],
    ["kazamata", "nagy", "A melyseg kiralynoje", "Liora", "Arin", "Selia", "Nerun", "Torak", "Priestess Selia"]
]

game_gyujt = [
    "Arin",
    "Liora",
    "Selia",
    "Nerun",
    "Torak",
    "Emera",
    "Kael",
    "Myra",
    "Thalen",
    "Isara",
]

kiv_kaz = -1
    
def game_mode():
    for kartya in game_kartyak:
        if not kartya[0]:
            cards.new_card(kartya)
        else:
            cards.game_vezer(kartya)
    for kaz in game_kazamatak:
        kazamata.new_kazamata(kaz)
    for nev in game_gyujt:
        cards.add_to_collection(["kartya", nev])

    menu()
    




def cls():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    cls()
    cprint("Udvozollek a Damareen-ben!\n", "blue")
    cprint("Valassz az alabbi opciok kozul:\n", "green")
    cprint("   1: Start")
    cprint("   2: Hasznalati utasitas")
    cprint("   3: Vilagkartyak")
    cprint("   4: Kazamatak")
    cprint("  ESC: Kilepes", "red")
    while True:
        #time.sleep(0.2)
        if keyboard.is_pressed("1"):
            game()
            break
        if keyboard.is_pressed("2"):
            guide()
            break
        if keyboard.is_pressed("esc"):
            cls()
            cprint("Kilepes...", "red")
            print("")
            break
        if keyboard.is_pressed("3"):
            vilagkartyak()
        if keyboard.is_pressed("4"):
            dungeon()

def guide():
    cls()
    cprint("Tarts be minden szabalyt:\n".center(os.get_terminal_size().columns), "red")
    cprint("A menuben szamokkal tudsz tovabblepni.".center(os.get_terminal_size().columns), "blue")
    cprint("Vard vegig a toltest.".center(os.get_terminal_size().columns), "blue")
    cprint("Az ESC gombbal tudsz visszalepni egyes menukbol.".center(os.get_terminal_size().columns), "blue")
    cprint("A jatekbol nem lehet kilepni, csak ha lefutott.".center(os.get_terminal_size().columns), "blue")
    cprint("A kartyak megadasa elott torold ki a beirt szamokat.".center(os.get_terminal_size().columns), "blue")
    cprint("A harc soran Enter-rel tudsz tovabblepni.".center(os.get_terminal_size().columns), "blue")

    print("")
    cprint("Nyomja meg az Enter-t a folytatashoz.".center(os.get_terminal_size().columns), "blue")
    input()
    menu()
    
def dungeon():
    cls()
    cprint("KAZAMATAK".center(os.get_terminal_size().columns), "green")
    print("\n")

    for i in range(len(game_kazamatak)):
        cprint(f"{game_kazamatak[i][2]}".center(os.get_terminal_size().columns), "blue")
        if game_kazamatak[i][1] == "egyszeru":
            cprint("Egyszeru szintu kazamata".center(os.get_terminal_size().columns), "green")
        elif game_kazamatak[i][1] == "kis":
            cprint("Kis szintu kazamata".center(os.get_terminal_size().columns), "green")
        else:
            cprint("Nagy szintu kazamata".center(os.get_terminal_size().columns), "green")
        cprint("Tag(ok):".center(os.get_terminal_size().columns), "green")
        for j in range(3, len(game_kazamatak[i]) - 1):
            print(game_kazamatak[i][j].center(os.get_terminal_size().columns))
        if game_kazamatak[i][1] == "egyszeru" or game_kazamatak[i][1] == "kis":
            cprint(f"Jutalom: {game_kazamatak[i][len(game_kazamatak[i]) - 1]}".center(os.get_terminal_size().columns), "green")
        else:
            cprint(f"Jutalom: kartya".center(os.get_terminal_size().columns), "green")
        print("")
    print("")
    cprint("Nyomja meg az Enter-t a folytatashoz.".center(os.get_terminal_size().columns), "blue")
    input()
    menu()

def vilagkartyak():
    cls()
    printed = 0
    for i in range(0, len(game_kartyak), 3):
        if len(game_kartyak) - printed >= 3:
            print(" ________________        ________________        ________________".center(os.get_terminal_size().columns))
            print(f"|{game_kartyak[i][1].center(16)}|      |{game_kartyak[i + 1][1].center(16)}|      |{game_kartyak[i + 2][1].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("vezer" if game_kartyak[i][0] else "sima").center(16)}|      |{("vezer" if game_kartyak[i + 1][0] else "sima").center(16)}|      |{("vezer" if game_kartyak[i + 2][0] else "sima").center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(game_kartyak[i][2]) + "  E  " + str(game_kartyak[i][3])).center(16)}|      |{("S  " + str(game_kartyak[i + 1][2]) + "  E  " + str(game_kartyak[i + 1][3])).center(16)}|      |{("S  " + str(game_kartyak[i + 2][2]) + "  E  " + str(game_kartyak[i + 2][3])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{game_kartyak[i][4].center(16)}|      |{game_kartyak[i + 1][4].center(16)}|      |{game_kartyak[i + 2][4].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 3
        elif len(cards.gyujtemeny) - printed == 2:
            print(" ________________        ________________".center(os.get_terminal_size().columns))
            print(f"|{game_kartyak[i][1].center(16)}|      |{game_kartyak[i+1][1].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("vezer" if game_kartyak[i][0] else "sima").center(16)}|      |{("vezer" if game_kartyak[i + 1][0] else "sima").center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(game_kartyak[i][23]) + "  E  " + str(game_kartyak[i][3])).center(16)}|      |{("S  " + str(game_kartyak[i + 1][2]) + "  E  " + str(game_kartyak[i + 1][3])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{game_kartyak[i][4].center(16)}|      |{game_kartyak[i + 1][4].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 2
        else:
            print(" ________________".center(os.get_terminal_size().columns))
            print(f"|{game_kartyak[i][1].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("vezer" if game_kartyak[i][0] else "sima").center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{("S  " + str(game_kartyak[i][2]) + "  E  " + str(game_kartyak[i][3])).center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{game_kartyak[i][4].center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 1
    print("")
    cprint("Nyomja meg az Enter-t a folytatashoz.".center(os.get_terminal_size().columns), "blue")
    input("")
    menu()
    


def game():
    cls()
    frame = 100
    current_frame = 0
    while True:
        #time.sleep(0.05)
        current_frame += 1
        cls()
        text = current_frame * "*" + (frame - current_frame) * " "
        cprint(text.center(os.get_terminal_size().columns), "green")
        if current_frame == frame:
            break
    kazamata_chooser()



def kazamata_chooser():
    cls()
    cprint("Valasszon kazamatat!".center(os.get_terminal_size().columns), "blue")
    index = 1
    choice = -1
    for kaz in kazamata.kazamatak:
        print("     ____________________".center(os.get_terminal_size().columns))
        print(f"     |{kaz["nev"].center(20)}|".center(os.get_terminal_size().columns))
        print(f"{index}.   |{kaz["tipus"].center(20)}|".center(os.get_terminal_size().columns))
        if kaz["tipus"] != "nagy":
            print(f"     |{kaz["fejlesztes"].center(20)}|".center(os.get_terminal_size().columns))
        else:
            print(f"     |{"uj kartya".center(20)}|".center(os.get_terminal_size().columns))
        print("     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
        index += 1
    while True:
        if keyboard.is_pressed("1"):
            kiv_kaz = 1
            choice = 1
            break
            
        if keyboard.is_pressed("2"):
            kiv_kaz = 2
            choice = 2
            break
            
        if keyboard.is_pressed("3"):
            kiv_kaz = 3
            choice = 3
            break
        if keyboard.is_pressed("esc"):
            choice = 4
            break
    
    if choice == 1:
        kartyacheck(kiv_kaz)
    elif choice == 2:
        kartyacheck(kiv_kaz)
    elif choice == 3:
        kartyacheck(kiv_kaz)
    elif choice == 4:
        menu()
            

def kartyacheck(kiv_kaz):
    if kazamata.kazamatak[kiv_kaz - 1]["tipus"] == "nagy":
        for nev in kazamata.kazamatak[kiv_kaz - 1]["kartyak"]:
            if cards.get_gyujt_stats(nev) == False and not cards.stats(nev)["vezer"]:
                pakliallito(kiv_kaz)
                return
        cls()
        print("Nem valaszthatod ezt a kazamatat,".center(os.get_terminal_size().columns))
        print("mert nincs olyan kartya,".center(os.get_terminal_size().columns))
        print("amit megszerezhetsz.".center(os.get_terminal_size().columns))
        print("\n")
        cprint("Nyomja meg az Enter-t a folytatashoz.".center(os.get_terminal_size().columns), "blue")
        input("")
        kazamata_chooser()
    else:
        cls()
        pakliallito(kiv_kaz)


def pakliallito(kiv_kaz):
    cls()
    printed = 0
    for i in range(0, len(cards.gyujtemeny), 3):
        if len(cards.gyujtemeny) - printed >= 3:
            print(" ________________        ________________        ________________".center(os.get_terminal_size().columns))
            print(f"|{" ".center(16)}|      |{" ".center(16)}|      |{" ".center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujtemeny[i].center(16)}|      |{cards.gyujtemeny[i + 1].center(16)}|      |{cards.gyujtemeny[i + 2].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{" ".center(16)}|      |{" ".center(16)}|      |{" ".center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 3
        elif len(cards.gyujtemeny) - printed == 2:
            print(" ________________        ________________".center(os.get_terminal_size().columns))
            print(f"|{" ".center(16)}|      |{" ".center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujtemeny[i].center(16)}|      |{cards.gyujtemeny[i + 1].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{" ".center(16)}|      |{" ".center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 2
        else:
            print(" ________________".center(os.get_terminal_size().columns))
            print(f"|{" ".center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{cards.gyujtemeny[i].center(16)}|".center(os.get_terminal_size().columns))
            print(f"|{" ".center(16)}|".center(os.get_terminal_size().columns))
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
            printed += 1
    
    print("")
    
    
    cprint(f"Adja meg szokozokkel elvalasztva a kivalasztott kartyak nevet sorrendben, max. {round(len(cards.gyujtemeny) / 2)}".center(os.get_terminal_size().columns), "blue")
    while True:
        egyediek = set()
        if keyboard.is_pressed("esc"):
            menu()
            break
        is_pakli_ready = True
        choice = input()
        valasztottak = choice.strip().split(" ")
        for valasztott in valasztottak:
            egyediek.add(valasztott)
            if len(valasztottak) > round(len(cards.gyujtemeny) / 2):
                cprint("Tul sokat adott meg!".center(os.get_terminal_size().columns), "red")
                is_pakli_ready = False
                break
            if cards.get_gyujt_stats(valasztott) == False:
                cprint("Adja meg a kartyakat helyesen!".center(os.get_terminal_size().columns), "red")
                is_pakli_ready = False
                break
            
        if len(egyediek) < len(valasztottak):
            cprint("Ne adjon meg tobb egyforma kartyat!".center(os.get_terminal_size().columns), "red")
            is_pakli_ready = False
        if is_pakli_ready:
            break
    
    cards.pakli = valasztottak
    harc(kiv_kaz)
        
        
def harc(kiv_kaz):
    cls()
    ellenfelek = kazamata.kazamatak[kiv_kaz - 1]["kartyak"]
    indexk = 0
    indexj = 0
    jatekh = cards.get_gyujt_stats(cards.pakli[indexj]).copy()
    kazh = cards.stats(ellenfelek[indexk]).copy()
    while True:
        if keyboard.is_pressed("esc"):
            menu()
        if indexk >= len(ellenfelek):
            input()
            win_screen(kiv_kaz, True, indexj)
        if indexj >= len(cards.pakli):
            input()
            win_screen(kiv_kaz, False, indexj)
        print(" ________________        ________________".center(os.get_terminal_size().columns))
        print(f"|{jatekh["nev"].center(16)}|      |{kazh["nev"].center(16)}|".center(os.get_terminal_size().columns))
        print(f"|{("S  " + str(jatekh["sebzes"]) + "  E  " + str(jatekh["eletero"])).center(16)}|      |{("S  " + str(kazh["sebzes"]) + "  E  " + str(kazh["eletero"])).center(16)}|".center(os.get_terminal_size().columns))
        print(f"|{jatekh["tipus"].center(16)}|      |{cards.stats(kazh["nev"])["tipus"].center(16)}|".center(os.get_terminal_size().columns))
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾".center(os.get_terminal_size().columns))
# ! #################################################################################################################################################
    # ! MARADJ A FOR CIKLUSBAN
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
    menu()