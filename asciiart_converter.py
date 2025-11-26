from termcolor import colored, cprint
zero = [
     "⣎⣵",
     "⠫⠜"
]
one = [
     "⢺ ",
     "⠼⠄"
]
two = [
     "⠊⡱",
     "⠮⠤"
]
three = [
     "⢉⡹",
     "⠤⠜"
]
four = [
     "⢇⣸",
     " ⠸"
]
five = [
     "⣏⡉",
     "⠤⠜"
]
six = [
     "⣎⡁",
     "⠣⠜"
]
seven = [
     "⠉⡹",
     "⠸ "
]
eight = [
     "⢎⡱",
     "⠣⠜"
]
nine = [
     "⢎⣱",
     "⠠⠜"
]



A = [
     "⣎⣱",
     "⠇⠸"
]
B = [
     "⣏⡱",
     "⠧⠜"
]
C = [
     "⡎⠑",
     "⠣⠔"
]
D = [
     "⡏⢱",
     "⠧⠜"
]
E = [
     "⣏⡉",
     "⠧⠤"
]
F = [
     "⣏⡉",
     "⠇ "
]
G = [
     "⡎⠑",
     "⠣⠝"
]
H = [
     "⣇⣸",
     "⠇⠸"
]
I = [
     "⡇",
     "⠇"
]
J = [
     "⠈⢹",
     "⠣⠜"
]
K = [
     "⣇⠜",
     "⠇⠱"
]
L = [
     "⡇ ",
     "⠧⠤"
]
M = [
     "⡷⢾",
     "⠇⠸"
]
N = [
     "⡷⣸",
     "⠇⠹"
]
O = [
     "⡎⢱",
     "⠣⠜"
]
P = [
     "⣏⡱",
     "⠇ "
]
Q = [
     "⡎⢱",
     "⠣⠪"
]
R = [
     "⣏⡱",
     "⠇⠱"
]
S = [
     "⢎⡑",
     "⠢⠜"
]
T = [
     "⢹⠁",
     "⠸ "
]
U = [
     "⡇⢸",
     "⠣⠜"
]
V = [
     "⡇⢸",
     "⠸⠃"
]
W = [
     "⡇⢸",
     "⠟⠻"
]
X = [
     "⢇⡸",
     "⠇⠸"
]
Y = [
     "⢇⢸",
     " ⠇"
]
Z = [
     "⢉⠝",
     "⠮⠤"
]

a = [
     "⢀⣀",
     "⠣⠼"
]
b = [
     "⣇⡀",
     "⠧⠜"
]
c = [
     "⢀⣀",
     "⠣⠤"
]
d = [
     "⢀⣸",
     "⠣⠼"
]
e = [
     "⢀⡀",
     "⠣⠭"
]
f = [
     "⣰⡁",
     "⢸ "
]
g = [
     "⢀⡀",
     "⣑⡺"
]
h = [
     "⣇⡀",
     "⠇⠸"
]
i = [
     "⠄",
     "⠇"
]
j = [
     "⠠",
     "⡸"
]
k = [
     "⡇⡠",
     "⠏⠢"
]
l = [
     "⡇",
     "⠣"
]
m = [
     "⣀⣀ ",
     "⠇⠇⠇"
]
n = [
     "⣀⡀",
     "⠇⠸"
]
o = [
     "⢀⡀",
     "⠣⠜"
]
p = [
     "⣀⡀",
     "⡧⠜"
]
q = [
     "⢀⣀",
     "⠣⢼"
]
r = [
     "⡀⣀",
     "⠏ "
]
s = [
     "⢀⣀",
     "⠭⠕"
]
t = [
     "⣰⡀",
     "⠘⠤"
]
u = [
     "⡀⢀",
     "⠣⠼"
]
v = [
     "⡀⢀",
     "⠱⠃"
]
w = [
     "⡀ ⢀",
     "⠱⠱⠃"
]
x = [
     "⡀⢀",
     "⠜⠣"
]
y = [
     "⡀⢀",
     "⣑⡺"
]
z = [
     "⣀⣀",
     "⠴⠥"
]




def text_to_ascii(text, int):
     ascii_text = ["", ""]
     for letter in text:
          if letter == "0":
               ascii_text[0] += zero[0] + " "
               ascii_text[1] += zero[1] + " "
          elif letter == "1":
               ascii_text[0] += one[0] + " "
               ascii_text[1] += one[1] + " "
          elif letter == "2":
               ascii_text[0] += two[0] + " "
               ascii_text[1] += two[1] + " "
          elif letter == "3":
               ascii_text[0] += three[0] + " "
               ascii_text[1] += three[1] + " "
          elif letter == "4":
               ascii_text[0] += four[0] + " "
               ascii_text[1] += four[1] + " "
          elif letter == "5":
               ascii_text[0] += five[0] + " "
               ascii_text[1] += five[1] + " "
          elif letter == "6":
               ascii_text[0] += six[0] + " "
               ascii_text[1] += six[1] + " "
          elif letter == "7":
               ascii_text[0] += seven[0] + " "
               ascii_text[1] += seven[1] + " "
          elif letter == "8":
               ascii_text[0] += eight[0] + " "
               ascii_text[1] += eight[1] + " "
          elif letter == "9":
               ascii_text[0] += nine[0] + " "
               ascii_text[1] += nine[1] + " "
          elif letter == "A":
               ascii_text[0] += A[0] + " "
               ascii_text[1] += A[1] + " "
          elif letter == "B":
               ascii_text[0] += B[0] + " "
               ascii_text[1] += B[1] + " "
          elif letter == "C":
               ascii_text[0] += C[0] + " "
               ascii_text[1] += C[1] + " "
          elif letter == "D":
               ascii_text[0] += D[0] + " "
               ascii_text[1] += D[1] + " "
          elif letter == "E":
               ascii_text[0] += E[0] + " "
               ascii_text[1] += E[1] + " "
          elif letter == "F":
               ascii_text[0] += F[0] + " "
               ascii_text[1] += F[1] + " "
          elif letter == "G":
               ascii_text[0] += G[0] + " "
               ascii_text[1] += G[1] + " "
          elif letter == "H":
               ascii_text[0] += H[0] + " "
               ascii_text[1] += H[1] + " "
          elif letter == "I":
               ascii_text[0] += I[0] + " "
               ascii_text[1] += I[1] + " "
          elif letter == "J":
               ascii_text[0] += J[0] + " "
               ascii_text[1] += J[1] + " "
          elif letter == "K":
               ascii_text[0] += K[0] + " "
               ascii_text[1] += K[1] + " "
          elif letter == "L":
               ascii_text[0] += L[0] + " "
               ascii_text[1] += L[1] + " "
          elif letter == "M":
               ascii_text[0] += M[0] + " "
               ascii_text[1] += M[1] + " "
          elif letter == "N":
               ascii_text[0] += N[0] + " "
               ascii_text[1] += N[1] + " "
          elif letter == "O":
               ascii_text[0] += O[0] + " "
               ascii_text[1] += O[1] + " "
          elif letter == "P":
               ascii_text[0] += P[0] + " "
               ascii_text[1] += P[1] + " "
          elif letter == "Q":
               ascii_text[0] += Q[0] + " "
               ascii_text[1] += Q[1] + " "
          elif letter == "R":
               ascii_text[0] += R[0] + " "
               ascii_text[1] += R[1] + " "
          elif letter == "S":
               ascii_text[0] += S[0] + " "
               ascii_text[1] += S[1] + " "
          elif letter == "T":
               ascii_text[0] += T[0] + " "
               ascii_text[1] += T[1] + " "
          elif letter == "U":
               ascii_text[0] += U[0] + " "
               ascii_text[1] += U[1] + " "
          elif letter == "V":
               ascii_text[0] += V[0] + " "
               ascii_text[1] += V[1] + " "
          elif letter == "W":
               ascii_text[0] += W[0] + " "
               ascii_text[1] += W[1] + " "
          elif letter == "X":
               ascii_text[0] += X[0] + " "
               ascii_text[1] += X[1] + " "
          elif letter == "Y":
               ascii_text[0] += Y[0] + " "
               ascii_text[1] += Y[1] + " "
          elif letter == "Z":
               ascii_text[0] += Z[0] + " "
               ascii_text[1] += Z[1] + " "
          elif letter == "a":
               ascii_text[0] += a[0] + " "
               ascii_text[1] += a[1] + " "
          elif letter == "b":
               ascii_text[0] += b[0] + " "
               ascii_text[1] += b[1] + " "
          elif letter == "c":
               ascii_text[0] += c[0] + " "
               ascii_text[1] += c[1] + " "
          elif letter == "d":
               ascii_text[0] += d[0] + " "
               ascii_text[1] += d[1] + " "
          elif letter == "e":
               ascii_text[0] += e[0] + " "
               ascii_text[1] += e[1] + " "
          elif letter == "f":
               ascii_text[0] += f[0] + " "
               ascii_text[1] += f[1] + " "
          elif letter == "g":
               ascii_text[0] += g[0] + " "
               ascii_text[1] += g[1] + " "
          elif letter == "h":
               ascii_text[0] += h[0] + " "
               ascii_text[1] += h[1] + " "
          elif letter == "i":
               ascii_text[0] += i[0] + " "
               ascii_text[1] += i[1] + " "
          elif letter == "j":
               ascii_text[0] += j[0] + " "
               ascii_text[1] += j[1] + " "
          elif letter == "k":
               ascii_text[0] += k[0] + " "
               ascii_text[1] += k[1] + " "
          elif letter == "l":
               ascii_text[0] += l[0] + " "
               ascii_text[1] += l[1] + " "
          elif letter == "m":
               ascii_text[0] += m[0] + " "
               ascii_text[1] += m[1] + " "
          elif letter == "n":
               ascii_text[0] += n[0] + " "
               ascii_text[1] += n[1] + " "
          elif letter == "o":
               ascii_text[0] += o[0] + " "
               ascii_text[1] += o[1] + " "
          elif letter == "p":
               ascii_text[0] += p[0] + " "
               ascii_text[1] += p[1] + " "
          elif letter == "q":
               ascii_text[0] += q[0] + " "
               ascii_text[1] += q[1] + " "
          elif letter == "r":
               ascii_text[0] += r[0] + " "
               ascii_text[1] += r[1] + " "
          elif letter == "s":
               ascii_text[0] += s[0] + " "
               ascii_text[1] += s[1] + " "
          elif letter == "t":
               ascii_text[0] += t[0] + " "
               ascii_text[1] += t[1] + " "
          elif letter == "u":
               ascii_text[0] += u[0] + " "
               ascii_text[1] += u[1] + " "
          elif letter == "v":
               ascii_text[0] += v[0] + " "
               ascii_text[1] += v[1] + " "
          elif letter == "w":
               ascii_text[0] += w[0] + " "
               ascii_text[1] += w[1] + " "
          elif letter == "x":
               ascii_text[0] += x[0] + " "
               ascii_text[1] += x[1] + " "
          elif letter == "y":
               ascii_text[0] += y[0] + " "
               ascii_text[1] += y[1] + " "
          elif letter == "z":
               ascii_text[0] += z[0] + " "
               ascii_text[1] += z[1] + " "
          elif letter == " ":
               ascii_text[0] += "  "
               ascii_text[1] += "  "

     if int == 0:
          return ascii_text
     else:
          return fr"""
               {ascii_text[0]}          
               {ascii_text[1]}          
          """

def ascii_to_text(ascii_block: str) -> str:
    # Sorok szétválasztása, center whitespace eltávolítása
    lines = ascii_block.strip("\n").split("\n")

    # Ha az első sor üres
    if lines[0].strip() == "":
        lines = lines[1:]

    line1 = lines[0].rstrip()
    line2 = lines[1].rstrip()

    # összes karakter mapping + szélesség
    patterns = {}

    def add(ch, patt):
        patterns[ch] = {
            "top": patt[0],
            "bot": patt[1],
            "w": len(patt[0])
        }

    all_chars = {
        "0": zero, "1": one, "2": two, "3": three, "4": four, "5": five,
        "6": six, "7": seven, "8": eight, "9": nine,
        "A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H,
        "I": I, "J": J, "K": K, "L": L, "M": M, "N": N, "O": O, "P": P,
        "Q": Q, "R": R, "S": S, "T": T, "U": U, "V": V, "W": W, "X": X,
        "Y": Y, "Z": Z,
        "a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h,
        "i": i, "j": j, "k": k, "l": l, "m": m, "n": n, "o": o, "p": p,
        "q": q, "r": r, "s": s, "t": t, "u": u, "v": v, "w": w, "x": x,
        "y": y, "z": z
    }

    for ch, patt in all_chars.items():
        add(ch, patt)

    result = ""
    pos = 0
    length = len(line1)

    while pos < length:
        matched = False

        # Végigpróbálunk minden karaktert
        for ch, patt in patterns.items():
            pattern_w = patt["w"]
            if pos + pattern_w <= length:
                if line1[pos:pos+pattern_w] == patt["top"] and line2[pos:pos+pattern_w] == patt["bot"]:
                    result += ch
                    pos += pattern_w + 1  # +1 space
                    matched = True
                    break

        if not matched:
            # ha nem talál egyezést → lépjünk egyet, de jelezzük a hibát
            result += "?"
            pos += 1

    result = result.replace("?", "")
    return result
     

