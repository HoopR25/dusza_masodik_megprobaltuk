import cards
import kazamata
import export
import fight
mentesek = []

def read_file(filer):
    mentesek.clear()
    global vilag 
    global beallitasok
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
            elif data[0] == "mentes":
                addtomentesek(data)

def beallitas(data):
        beallitasok.append(data[1])
        beallitasok.append(data[2])
        beallitasok.append(data[3])


def addtomentesek(mentesnev):
    mentesek.append([mentesnev[1],beallitasok.copy(),cards.gyujtemeny.copy(),cards.gyujt_stats.copy(),cards.pakli.copy(),vilag])
    cards.gyujtemeny.clear()
    cards.gyujt_stats.clear()
    cards.pakli.clear()
    beallitasok.clear()
