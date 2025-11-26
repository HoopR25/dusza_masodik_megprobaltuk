import cards
import kazamata
import export
import fight
mentesek = []
beallitasok = []
vilag = ""
def read_file(file, arg):
    if arg[len(arg) - 1] != "/" or arg[len(arg) - 1] != "\\":
        arg += "/"
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
        beallitasok[0]=data[1]
        beallitasok[1]=data[2]
        beallitasok[2]=data[3]


def addtomentesek(mentesnev):
    mentesek.append([mentesnev,beallitasok,cards.gyujtemeny,cards.gyujt_stats,cards.pakli,vilag])
    cards.gyujtemeny.clear()
    cards.gyujt_stats.clear()
    cards.pakli.clear()
