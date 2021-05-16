# 3.3.3, Woche 3, Block 3, Aufgabe 3

# Import
from daten import woerterbuch

# Funktionen


def spiegeln(w):
    m = {}
    for i in range(len(list(w))):
        m[w[list(w)[i]]] = list(w)[i]
    return m


# Main
print(spiegeln(woerterbuch))
