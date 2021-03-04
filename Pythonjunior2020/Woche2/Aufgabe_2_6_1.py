# 2.6.1, Woche 2, Block 6, Aufgabe 1

# String 
satz = "Folgt?weiter?dem?Pfad"

# Split String 
satz = satz.split("?")
satz += ["."]

# String combine
ausgabe = ""
for i in range(len(satz)):
    ausgabe += satz[i] + " "

# Ausgabe String
print(ausgabe)