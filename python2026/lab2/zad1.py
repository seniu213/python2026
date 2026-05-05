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

all_common = set()
for gene in set_gene1:
    if gene in set_gene2 and gene in set_gene3:
        all_common.add(gene)

common_for_two = set()
for gene in set_gene1:
    if gene in set_gene2 and gene not in all_common:
        common_for_two.add(gene)
    if gene in set_gene3 and gene not in all_common:
        common_for_two.add(gene)

for gene in set_gene2:
    if gene in set_gene3 and gene not in all_common:
        common_for_two.add(gene)

all_genes = set()
for gene in set_gene1:
    all_genes.add(gene)
for gene in set_gene2:
    all_genes.add(gene)
for gene in set_gene3:
    all_genes.add(gene)

only_one_disease = set()
for gene in all_genes:
    count = 0
    if gene in set_gene1:
        count = count + 1
    if gene in set_gene2:
        count = count + 1
    if gene in set_gene3:
        count = count + 1

    if count == 1:
        only_one_disease.add(gene)

print("a) Wspolne dla wszystkich pacjentow:")
print(sorted(list(all_common)))
print()

print("b) Wspolne dokladnie dla 2 pacjentow:")
print(sorted(list(common_for_two)))
print()

print("c) Wystepuja tylko w 1 chorobie:")
print(sorted(list(only_one_disease)))