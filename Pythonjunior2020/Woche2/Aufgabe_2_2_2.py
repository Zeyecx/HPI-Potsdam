# 2.2.2, Woche 2, Block 2, Aufgabe 2

# Import 
from daten import hauptspeise, nachtisch

# IF-Statement
if hauptspeise == "Pommes" and nachtisch == "Schokoladenpudding":
    print("Simon")
elif hauptspeise != "Kartoffeln" and nachtisch == "Obstsalat":
    print("Leonie")
elif hauptspeise == "Kartoffeln" or hauptspeise == "Nudeln":
    if nachtisch == "Erdbeerjoghurt":
        print("Paul")
    else:
        print("Mia")
else:
    print("Mia")