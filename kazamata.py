kazamatak = []


def new_kazamata(kazamata):
    if kazamata[1] == "egyszeru" or kazamata[1] == "kis":
        nevek = kazamata[3].split(",")
        if kazamata[1] == "kis":
            nevek.append(kazamata[4])
        k = {
            "tipus": kazamata[1],
            "nev": kazamata[2],
            "kartyak": nevek,
            "fejlesztes": kazamata[len(kazamata) - 1]
        }
    else:
        nevek = kazamata[3].split(",")
        nevek.append(kazamata[len(kazamata) - 1])
        k = {
            "tipus": kazamata[1],
            "nev": kazamata[2],
            "kartyak": nevek,
        }
    kazamatak.append(k)
    
