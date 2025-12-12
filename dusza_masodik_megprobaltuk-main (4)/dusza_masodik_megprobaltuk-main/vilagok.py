import jatekmestermenu
import cards
import kazamata


def uj_vilag(data):
    jatekmestermenu.vilagok.append([data[1], cards.kartyak.copy(), cards.gyujtemeny.copy(), kazamata.kazamatak.copy()])
    cards.kartyak.clear()
    cards.gyujtemeny.clear()
    kazamata.kazamatak.clear()

