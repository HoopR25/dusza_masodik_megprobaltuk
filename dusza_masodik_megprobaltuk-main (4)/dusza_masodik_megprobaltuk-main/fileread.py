import cards
import kazamata
import export
import fight

def read_file(file, arg):
    if arg[len(arg) - 1] != "/" or arg[len(arg) - 1] != "\\":
        arg += "/"
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(";")
        if data[0] == "uj kartya":
            cards.new_card(data)
        elif data[0] == "uj vezer":
            cards.new_vezer(data)
        elif data[0] == "uj kazamata":
            kazamata.new_kazamata(data)
        elif data[0] == "felvetel gyujtemenybe":                                                              
            cards.add_to_collection(data)
        elif data[0] == "uj pakli":
            cards.new_deck(data) 
        elif data[0] == "harc":
            fight.fight(arg, data[1],data[2])
        elif data[0] == "export vilag" or data[0] == "export jatekos":
            export.export(arg, data)
            
