import cards
import kazamata

def export(arg, data):
    path = arg + data[1]
    if data[0] == "export vilag":
        with open (path, "w", encoding="utf-8") as file:
            for i in range(len(cards.kartyak)):
                kartya = cards.kartyak[i]
                if cards.kartyak[i]["vezer"] == False:
                    if i != len(cards.kartyak):
                        file.write(f"kartya;{kartya["nev"]};{kartya["sebzes"]};{kartya["eletero"]};{kartya["tipus"]}\n")
                    else:
                        file.write(f"kartya;{kartya["nev"]};{kartya["sebzes"]};{kartya["eletero"]};{kartya["tipus"]}")
            file.write("\n")
            for i in range(len(cards.kartyak)):
                kartya = cards.kartyak[i]
                if cards.kartyak[i]["vezer"] == True:
                    if i != len(cards.kartyak):
                        file.write(f"vezer;{kartya["nev"]};{kartya["sebzes"]};{kartya["eletero"]};{kartya["tipus"]}\n")
                    else:
                        file.write(f"vezer;{kartya["nev"]};{kartya["sebzes"]};{kartya["eletero"]};{kartya["tipus"]}")
            file.write("\n")
            for kazamata_belso in kazamata.kazamatak:
                if kazamata_belso["tipus"] != "nagy":
                    file.write(f"kazamata;{kazamata_belso["tipus"]};{kazamata_belso["nev"]};")
                    for i in range(len(kazamata_belso["kartyak"])):
                        if i != len(kazamata_belso["kartyak"]) - 1:
                            if kazamata_belso["tipus"] == "kis":
                                if i != len(kazamata_belso["kartyak"]) - 2:
                                    file.write(f"{kazamata_belso["kartyak"][i]},")
                                else:
                                    file.write(f"{kazamata_belso["kartyak"][i]};")
                            else:
                                file.write(f"{kazamata_belso["kartyak"][i]};")
                        else:
                            file.write(f"{kazamata_belso["kartyak"][i]};")
                    file.write(f"{kazamata_belso["fejlesztes"]}\n")
                else:
                    file.write(f"kazamata;{kazamata_belso["tipus"]};{kazamata_belso["nev"]};")
                    for i in range(len(kazamata_belso["kartyak"])):
                        if i != len(kazamata_belso["kartyak"]) - 2 and i != len(kazamata_belso["kartyak"]) - 1:
                            file.write(f"{kazamata_belso["kartyak"][i]},")
                        else:
                            if i != len(kazamata_belso["kartyak"]) - 1:
                                file.write(f"{kazamata_belso["kartyak"][i]};")
                            else:
                                file.write(f"{kazamata_belso["kartyak"][i]}\n")
    else:
        with open (path, "w", encoding="utf-8") as file:
            for kartya in cards.gyujtemeny:
                stat = cards.get_gyujt_stats(kartya)
                file.write(f"gyujtemeny;{kartya};{stat["sebzes"]};{stat["eletero"]};{stat["tipus"]}\n")
            file.write("\n")

            for i in range(len(cards.pakli)):
                if i != len(cards.pakli) - 1:
                    file.write(f"pakli;{cards.pakli[i]}\n")
                else:
                    file.write(f"pakli;{cards.pakli[i]}")

                
                            
