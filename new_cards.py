import cards

def new_card(kartya):
    card = {
        "nev": kartya["nev"],
        "sebzes": int(kartya["sebzes"]),
        "eletero": int(kartya["eletero"]),
        "tipus": kartya["tipus"],
        "vezer": False,
    }
    cards.kartyak.append(card)

def new_vezer(vezer):
    card = {
    "nev": vezer["nev"],
    "sebzes": int(vezer["sebzes"]) * 2,
    "eletero": int(vezer["eletero"]),
    "tipus": vezer["tipus"],
    "vezer": True,
    "szarmaztatas": vezer["szarmaztatas"],
    "duplazo": vezer["szarmaztatas"]
    }
    cards.vezerek.append(card)

def gyujtstatsmasolo(kartya):
    cards.gyujtemeny.append(kartya["nev"])
    card = {
        "nev": kartya["nev"],
        "sebzes": int(kartya["sebzes"]),
        "eletero": int(kartya["eletero"]),
        "tipus": kartya["tipus"],
        "vezer": False,
    }
    cards.gyujt_stats.append(card)


def add_to_collection(kartya):
    cards.gyujtemeny.append(kartya[1])
    st = stats(kartya[1])
    if st != None:
        cards.gyujt_stats.append(st)


def stats(nev):
    for kartya in cards.kartyak:
        if kartya["nev"] == nev:
            return kartya.copy()

def get_gyujt_stats(nev):
    for kartya in cards.gyujt_stats:
        if kartya["nev"] == nev:
            return kartya.copy()
    return False


def new_deck(nevek):
    cards.pakli.clear()
    data = nevek[1].split(",")
    for i in range(0, len(data)):
        cards.pakli.append(data[i])
        

def game_vezer(kartya):
    card = {
        "nev": kartya[1],
        "sebzes": int(kartya[2]),
        "eletero": int(kartya[3]),
        "tipus": kartya[4],
        "vezer": True,
    }
    cards.kartyak.append(card)
