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

for target in ("FGFR4", "FGERA4"):
    indices = [i for i, gene in enumerate(lista_gene1) if gene == target]
    if indices:
        print(f"Gen {target} wystepuje na indeksach: {indices}")
    else:
        print(f"Gen {target} nie wystepuje na liscie.")

