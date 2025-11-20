import cards
import kazamata
#pakli a cards.pakli

tipusok = ["fold", "levego", "viz", "tuz", "fold", "levego"]


def fight(arg, kazamatanev, fajlnev):
    

    jt = 0
    kt = 0
    kazamata_kor = True
    jatekos_nyert = True

    fejlesztes = {
        "eletero": 2,
        "sebzes": 1,
    }

    

    
    for kazam in kazamata.kazamatak:
        if kazam["nev"] == kazamatanev:
            kpakli = kazam["kartyak"]
            kstat = kazam.copy()
    jpakli = cards.pakli.copy()

    kazamath = cards.stats(kpakli[kt]).copy()
    jatekh = cards.get_gyujt_stats(jpakli[jt]).copy()
    kor = 1
    path = arg + fajlnev
    print(path)
    with open(path, "w", encoding="utf-8") as file:
        file.write(f"harc kezdodik;{kazamatanev}\n\n")
        file.write(f"{kor}.kor;kazamata;kijatszik;{kazamath["nev"]};{kazamath["sebzes"]};{kazamath["eletero"]};{kazamath["tipus"]}\n")
        file.write(f"{kor}.kor;jatekos;kijatszik;{jatekh["nev"]};{jatekh["sebzes"]};{jatekh["eletero"]};{jatekh["tipus"]}\n")
        kor += 1 
        while True:
            file.write("\n") 
            if kazamata_kor:
                if kazamath["tipus"] != jatekh["tipus"]:
                    ktipus = get_tipus_index(kazamath["tipus"])
                    jtipus = get_tipus_index(jatekh["tipus"])
                    if tipusok[ktipus] == tipusok[jtipus - 1] or tipusok[ktipus] == tipusok[jtipus + 1]:
                        jatekh["eletero"] -= kazamath["sebzes"] * 2
                        
                        file.write(f"{kor}.kor;kazamata;tamad;{kazamath["nev"]};{kazamath["sebzes"] * 2};{jatekh["nev"]};")
                    else:
                        jatekh["eletero"] -= int(kazamath["sebzes"] / 2)
                         
                        file.write(f"{kor}.kor;kazamata;tamad;{kazamath["nev"]};{int(kazamath["sebzes"] / 2)};{jatekh["nev"]};")
                else:
                    jatekh["eletero"] -= kazamath["sebzes"]
                    
                    file.write(f"{kor}.kor;kazamata;tamad;{kazamath["nev"]};{kazamath["sebzes"]};{jatekh["nev"]};")
                if jatekh["eletero"] <= 0:
                    jatekh["eletero"] = 0
                    file.write(f"{jatekh["eletero"]}\n")
                    jt += 1
                    if jt >= len(jpakli):
                        jatekos_nyert = False
                        break
                    
                    jatekh = cards.get_gyujt_stats(jpakli[jt]).copy()  
                    file.write(f"{kor}.kor;jatekos;kijatszik;{jatekh["nev"]};{jatekh["sebzes"]};{jatekh["eletero"]};{jatekh["tipus"]}\n")
                    kor += 1
                else:
                    file.write(f"{jatekh["eletero"]}\n")
                    if kazamath["tipus"] != jatekh["tipus"]:
                        ktipus = get_tipus_index(kazamath["tipus"])
                        jtipus = get_tipus_index(jatekh["tipus"])
                        if tipusok[ktipus] == tipusok[jtipus  - 1] or tipusok[ktipus] == tipusok[jtipus + 1]:
                            file.write(f"{kor}.kor;jatekos;tamad;{jatekh["nev"]};{jatekh["sebzes"] * 2};{kazamath["nev"]};")
                            kazamath["eletero"] -= jatekh["sebzes"] * 2
                        else:
                            file.write(f"{kor}.kor;jatekos;tamad;{jatekh["nev"]};{int(jatekh["sebzes"] / 2)};{kazamath["nev"]};")
                            kazamath["eletero"] -= int(jatekh["sebzes"] / 2)
                    else:
                        file.write(f"{kor}.kor;jatekos;tamad;{jatekh["nev"]};{jatekh["sebzes"]};{kazamath["nev"]};")
                        kazamath["eletero"] -= jatekh["sebzes"]
                    if kazamath["eletero"] <= 0:
                        kazamath["eletero"] = 0
                        
                        kt += 1
                        file.write(f"{kazamath["eletero"]}\n")
                        if kt >= len(kpakli):
                            jatekos_nyert = True
                            break
                        kazamata_kor = False
                        kor += 1
                        
                        kazamath = cards.stats(kpakli[kt]).copy()
                        
                        file.write(f"{kor}.kor;kazamata;kijatszik;{kazamath["nev"]};{kazamath["sebzes"]};{kazamath["eletero"]};{kazamath["tipus"]}\n")
                    else:
                        kor += 1
                        file.write(f"{kazamath["eletero"]}\n")
            # ! jatekos kezd
            else:
                if kazamath["tipus"] != jatekh["tipus"]:
                    ktipus = get_tipus_index(kazamath["tipus"])
                    jtipus = get_tipus_index(jatekh["tipus"])
                    if tipusok[ktipus] == tipusok[jtipus - 1] or tipusok[ktipus] == tipusok[jtipus + 1]:
                        kazamath["eletero"] -= jatekh["sebzes"] * 2
                        file.write(f"{kor}.kor;jatekos;tamad;{jatekh["nev"]};{jatekh["sebzes"] * 2};{kazamath["nev"]};")

                    else:
                        kazamath["eletero"] -= int(jatekh["sebzes"] / 2)
                        file.write(f"{kor}.kor;jatekos;tamad;{jatekh["nev"]};{int(jatekh["sebzes"] / 2)};{kazamath["nev"]};")
                        
                else:
                    kazamath["eletero"] -= jatekh["sebzes"]
                    file.write(f"{kor}.kor;jatekos;tamad;{jatekh["nev"]};{jatekh["sebzes"]};{kazamath["nev"]};")
                    
                if kazamath["eletero"] <= 0:
                    kor += 1
                    kazamath["eletero"] = 0
                    file.write(f"{kazamath["eletero"]}\n")
                    kt += 1
                    if kt >= len(kpakli):
                        jatekos_nyert = True
                        break
                    kazamath = cards.stats(kpakli[kt]).copy()
                    file.write(f"{kor}.kor;kazamata;kijatszik;{kazamath["nev"]};{kazamath["sebzes"]};{kazamath["eletero"]};{kazamath["tipus"]}\n")
                else:
                    kor += 1
                    file.write(f"{kazamath["eletero"]}\n")
                    if kazamath["tipus"] != jatekh["tipus"]:
                        ktipus = get_tipus_index(kazamath["tipus"])
                        jtipus = get_tipus_index(jatekh["tipus"])
                        if tipusok[ktipus] == tipusok[jtipus - 1] or tipusok[ktipus] == tipusok[jtipus + 1]:
                            jatekh["eletero"] -= kazamath["sebzes"] * 2
                            file.write(f"{kor}.kor;kazamata;tamad;{kazamath["nev"]};{kazamath["sebzes"] * 2};{jatekh["nev"]};")
                        else:
                            jatekh["eletero"] -= int(kazamath["sebzes"] / 2)
                            file.write(f"{kor}.kor;kazamata;tamad;{kazamath["nev"]};{int(kazamath["sebzes"] / 2)};{jatekh["nev"]};")
                    else:
                        jatekh["eletero"] -= kazamath["sebzes"]
                        file.write(f"{kor}.kor;kazamata;tamad;{kazamath["nev"]};{kazamath["sebzes"]};{jatekh["nev"]};")
                    if jatekh["eletero"] <= 0:
                        jatekh["eletero"] = 0
                        file.write(f"{jatekh["eletero"]}\n")
                        jt += 1
                        if jt >= len(jpakli):
                            jatekos_nyert = False
                            break
                            
                        kazamata_kor = True
                        kor += 1
                        jatekh = cards.stats(jpakli[jt]).copy()
                        file.write(f"{kor}.kor;jatekos;kijatszik;{jatekh["nev"]};{jatekh["sebzes"]};{jatekh["eletero"]};{jatekh["tipus"]}\n")

                    else:
                        kor += 1
        #vege a whilenak
        if (kstat["tipus"] == "egyszeru" or kstat["tipus"] == "kis") and jatekos_nyert: 
            file.write(f"\njatekos nyert;{kstat["fejlesztes"]};{jatekh["nev"]}")
            for i in range(len(cards.gyujt_stats)):
                if cards.gyujt_stats[i]["nev"] == jpakli[jt]:
                    cards.gyujt_stats[i][kstat["fejlesztes"]] += fejlesztes[kstat["fejlesztes"]]
                    break
        elif jatekos_nyert:
            for kartya in kpakli:
                if(cards.get_gyujt_stats(kartya)==False):
                    cards.add_to_collection(["", kartya])
                    file.write(f"\njatekos nyert;{kartya}")
                    break
        else:
            file.write(f"\njatekos vesztett")

def get_tipus_index(tipus):
    for i in range(1, 5):
        if tipusok[i] == tipus:
            return i