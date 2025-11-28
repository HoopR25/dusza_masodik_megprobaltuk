kazamatak = []
import kazamata

def new_kazamata(kazamatat):
    if kazamatat["tipus"] == "egyszeru" or kazamatat["tipus"] == "kis":
        nevek = kazamatat["kartyak"]
        k = {
            "tipus": kazamatat["tipus"],
            "nev": kazamatat["nev"],
            "kartyak": nevek,
            "fejlesztes": kazamatat["fejlesztes"]
        }
    else:
        nevek = kazamatat["kartyak"]
        k = {
            "tipus": kazamatat["tipus"],
            "nev": kazamatat["nev"],
            "kartyak": nevek,
        }
    kazamata.kazamatak.append(k)


