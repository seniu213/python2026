# Zadanie 2: sprawdz czy geny FGFR4 i FGERA4 wystepuja na liscie oraz podaj ich indeksy.
lista_gene1 = [
    "SLC19A2",
    "ATP7B",
    "ERBB3",
    "FGFR14",
    "ABCC3",
    "GALNT14",
    "ERCC1",
    "LJS19A2",
    "AKM7B",
    "ELLB34",
    "FULR4",
    "ANGC3",
    "WELNT14",
    "EOO1",
    "SAC19A22",
    "FGFR4",
    "ERB3",
    "FGR4",
    "FGFR4",
    "GASNT14",
    "ERSS4",
]

target = "FGFR4"
indices = []
for i in range(len(lista_gene1)):
    if lista_gene1[i] == target:
        indices.append(i)

if len(indices) > 0:
    print("Gen " + target + " wystepuje na indeksach: " + str(indices))
else:
    print("Gen " + target + " nie wystepuje na liscie.")

target = "FGERA4"
indices = []
for i in range(len(lista_gene1)):
    if lista_gene1[i] == target:
        indices.append(i)

if len(indices) > 0:
    print("Gen " + target + " wystepuje na indeksach: " + str(indices))
else:
    print("Gen " + target + " nie wystepuje na liscie.")
