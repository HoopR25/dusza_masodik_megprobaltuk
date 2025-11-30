import cards
import kazamata
import export
import fight
import new_cards
import jatekmestermenu
mentesek = []

def read_file(filer):
    mentesek.clear()
    global vilag 
    global beallitasok
    cards.gyujtemeny.clear()
    cards.gyujt_stats.clear()
    cards.pakli.clear()
    cards.vezerek.clear()
    cards.kartyak.clear()
    beallitasok = []
    with open(filer, "r", encoding = "utf-8") as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(";")
            if data[0] == "uj kartya":
                cards.new_card(data)
            elif data[0] == "felvetel gyujtemenybe":                                                              
                cards.add_to_collection(data)
            elif data[0] == "uj pakli":
                cards.new_deck(data) 
            elif data[0] == "beallitasok":
                beallitas(data)
            elif data[0] == "vilag":
                vilag = data[1]
                for vilag2 in jatekmestermenu.vilagok:
                    if vilag2[0] == vilag:
                        
                        vilagnev = vilag2[0]
                        for kartya in vilag2[1]:
                            if kartya["vezer"]:
                                new_cards.new_vezerf(kartya)
                            else:
                                new_cards.new_cardf(kartya)
            elif data[0] == "mentes":
                addtomentesek(data)
            elif data[0] == "stats":
                new_cards.statmodositas(data)

def beallitas(data):
        global beallitasok
        beallitasok.append(data[1])
        beallitasok.append(data[2])


def addtomentesek(mentesnev):
    global beallitasok
    mentesek.append([mentesnev[1],beallitasok.copy(),cards.gyujtemeny.copy(),cards.gyujt_stats.copy(),cards.pakli.copy(),vilag])
    cards.gyujtemeny.clear()
    cards.gyujt_stats.clear()
    cards.pakli.clear()
    cards.vezerek.clear()
    cards.kartyak.clear()
    beallitasok.clear()
