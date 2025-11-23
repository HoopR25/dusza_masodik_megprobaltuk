import cards
import kazamata
import export
import fight
import vilagok

def read_file(file):
    f = open(file, "r", encoding = "utf-8")
    lines = f.readlines()
    for line in lines:
        data = line.strip().split(";")
        if data[0] == "uj vilag":
            vilagok.uj_vilag(data)
        elif data[0] == "uj kartya":
            cards.new_card(data)
        elif data[0] == "uj vezer":
            cards.new_vezer(data)
        elif data[0] == "uj kazamata":
            kazamata.new_kazamata(data)
        elif data[0] == "felvetel gyujtemenybe":                                                              
            cards.add_to_collection(data)
        elif data[0] == "uj pakli":
            cards.new_deck(data) 
    f.close()
