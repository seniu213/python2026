# Zadanie 1: znajdz geny wspolne dla 3 pacjentow, wspolne dla 2 pacjentow oraz wystepujace tylko w 1 chorobie.
set_gene1 = {
    "SLC19A2",
    "ATP7B",
    "ERBB3",
    "FGFR4",
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
    "AAAP7B",
    "ERB3",
    "FGR4",
    "ACC3",
    "GASNT14",
    "ERSS4",
}

set_gene2 = {
    "SLC19A3",
    "ATP7B",
    "ERBB3",
    "FGFR4",
    "ABCC3",
    "GALNT14",
    "ERCC1",
    "LJS19A2",
    "AKM7B",
    "ELLB32",
    "FULR421",
    "ANGC3",
    "WELNT14",
    "EOO11",
    "SAC19A2",
    "AAAP7B",
    "ERB3",
    "FGR4",
    "ACC3",
    "GASNT14",
    "ERSS4",
}

set_gene3 = {
    "SLC19A3",
    "ATP7B1",
    "ERBB32",
    "FGFR4",
    "ABCC3",
    "GALNT14",
    "ERCC11",
    "LJS19A2",
    "AKM7B",
    "ELLB34",
    "FULR4",
    "ANGC3",
    "WELNT15",
    "EOO1",
    "SAC19A22",
    "AAP7B",
    "ERBB3",
    "FGR4",
    "ACC4",
    "GASNT14",
    "ERSS4",
}

all_common = set_gene1 & set_gene2 & set_gene3
common_for_two = ((set_gene1 & set_gene2) | (set_gene1 & set_gene3) | (set_gene2 & set_gene3)) - all_common

counts = {}
for gene in set_gene1 | set_gene2 | set_gene3:
    counts[gene] = int(gene in set_gene1) + int(gene in set_gene2) + int(gene in set_gene3)
only_one_disease = {gene for gene, count in counts.items() if count == 1}

print("a) Wspolne dla wszystkich pacjentow:")
print(sorted(all_common))
print()

print("b) Wspolne dokladnie dla 2 pacjentow:")
print(sorted(common_for_two))
print()

print("c) Wystepuja tylko w 1 chorobie:")
print(sorted(only_one_disease))

