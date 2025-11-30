kartyak = []
gyujtemeny = []
pakli = []
gyujt_stats = []
vezerek = []
def new_card(kartya):
    card = {
        "nev": kartya[1],
        "sebzes": int(kartya[2]),
        "eletero": int(kartya[3]),
        "tipus": kartya[4],
        "vezer": False,
    }
    kartyak.append(card)

def new_vezer(vezer):
    for kartya in kartyak:
        if kartya["nev"] == vezer[2]:
            if vezer[3] == "sebzes":
                card = {
                    "nev": vezer[1],
                    "sebzes": int(kartya["sebzes"]) * 2,
                    "eletero": int(kartya["eletero"]),
                    "tipus": kartya["tipus"],
                    "vezer": True,
                    "szarmaztatas": vezer[2],
                    "duplazo": vezer[3],
                }
                kartyak.append(card)

            else:
                card = {
                    "nev": vezer[1],
                    "sebzes": int(kartya["sebzes"]),
                    "eletero": int(kartya["eletero"])* 2,
                    "tipus": kartya["tipus"],
                    "vezer": True,
                    "szarmaztatas": vezer[2],
                    "duplazo": vezer[3],
                }
                kartyak.append(card)

def add_to_collection(kartya):
    if kartya[1] not in gyujtemeny:
        gyujtemeny.append(kartya[1])
        st = stats(kartya[1])
        if st is not None:
            gyujt_stats.append(st)



def stats(nev):
    for kartya in kartyak:
        if kartya["nev"] == nev:
            return kartya.copy()
    for kartya in vezerek:
        if kartya["nev"] == nev:
            return kartya.copy()

def get_gyujt_stats(nev):
    for kartya in gyujt_stats:
        if kartya["nev"] == nev:
            return kartya.copy()
    return False


def new_deck(nevek):
    pakli.clear()
    data = nevek[1].split(",")
    for i in range(0, len(data)):
        pakli.append(data[i])
        

def game_vezer(kartya):
    card = {
        "nev": kartya[1],
        "sebzes": int(kartya[2]),
        "eletero": int(kartya[3]),
        "tipus": kartya[4],
        "vezer": True,
    }
    kartyak.append(card)