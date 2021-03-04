# 3.3.2, Woche 3, Block 3, Aufgabe 2 

# Import 
from daten import satz
from daten import woerterbuch

# Funktionen
def uebersetze(s):
    # Reset x
    x = []
    w = woerterbuch
    # Satz in Array umwandeln
    s = s.split(" ")

    # Gehe den Satz durch
    for i in range(len(s)):
        # Woertbuch[String[Iteration]]
        x.append(w[s[i]])

    # String combine
    for i in range(len(x)):
        if i == 0 :
            y = x[i]
        else:
            y += " "+x[i]

    # Return des Strings
    return y+"."

# Main
print(uebersetze(satz))