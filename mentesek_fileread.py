import cards
import kazamata
import export
import fight
mentesek = []
beallitasok = []
vilag = ""
def read_file(filer):
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
                addtomentesek(data[1])

def beallitas(data):
        beallitasok.append(data[1])
        beallitasok.append(data[2])
        beallitasok.append(data[3])


def addtomentesek(mentesnev):
    mentesek.append([mentesnev,beallitasok,cards.gyujtemeny,cards.gyujt_stats,cards.pakli,vilag])
    cards.gyujtemeny.clear()
    cards.gyujt_stats.clear()
    cards.pakli.clear()
